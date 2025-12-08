# Before/After White Balance Visualization
import numpy as np
import matplotlib.pyplot as plt


def visualize_white_balance_correction(images_before, images_after, frame_idx=0):
    """Visualize white balance correction with before/after comparison."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # Select frame to display
    before = images_before[frame_idx]
    after = images_after[frame_idx]
    
    # Row 1: Full images
    axes[0, 0].imshow(before)
    axes[0, 0].set_title(f'Before White Balance\nFrame {frame_idx}', fontsize=14, fontweight='bold')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(after)
    axes[0, 1].set_title(f'After White Balance\nFrame {frame_idx}', fontsize=14, fontweight='bold')
    axes[0, 1].axis('off')
    
    # Difference visualization
    diff = np.abs(after.astype(float) - before.astype(float))
    axes[0, 2].imshow(diff.astype(np.uint8))
    axes[0, 2].set_title('Absolute Difference\n(After - Before)', fontsize=14, fontweight='bold')
    axes[0, 2].axis('off')
    
    # Row 2: RGB histograms
    colors = ['red', 'green', 'blue']
    channel_names = ['Red', 'Green', 'Blue']
    
    for i in range(3):
        ax = axes[1, i]
        
        # Before histogram
        before_hist, bins = np.histogram(before[:, :, i].flatten(), bins=256, range=(0, 256))
        after_hist, _ = np.histogram(after[:, :, i].flatten(), bins=256, range=(0, 256))
        
        ax.plot(bins[:-1], before_hist, color=colors[i], alpha=0.5, linewidth=2, 
                label='Before', linestyle='--')
        ax.plot(bins[:-1], after_hist, color=colors[i], alpha=0.8, linewidth=2, 
                label='After')
        
        ax.set_title(f'{channel_names[i]} Channel Histogram', fontsize=12, fontweight='bold')
        ax.set_xlabel('Pixel Value')
        ax.set_ylabel('Frequency')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.suptitle('White Balance Correction: Before vs After', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.show()
    
    # Print statistics
    print("\n" + "="*70)
    print("WHITE BALANCE CORRECTION STATISTICS")
    print("="*70)
    print(f"\nFrame {frame_idx} Analysis:")
    print(f"\n{'Channel':<10} {'Before Mean':<15} {'After Mean':<15} {'Change':<10}")
    print("-" * 70)
    
    for i, name in enumerate(['Red', 'Green', 'Blue']):
        before_mean = before[:, :, i].mean()
        after_mean = after[:, :, i].mean()
        change = after_mean - before_mean
        print(f"{name:<10} {before_mean:>14.2f} {after_mean:>14.2f} {change:>+9.2f}")
    
    print("\n" + "="*70)


# Usage example (add this to your notebook after applying white balance):
"""
# Visualize white balance correction
print("\nVisualizing white balance correction...")
visualize_white_balance_correction(images, images_corrected, frame_idx=0)

# Also show a few more frames for comparison
print("\nShowing additional frames...")
for idx in [10, 30, 50]:
    if idx < len(images):
        visualize_white_balance_correction(images, images_corrected, frame_idx=idx)
"""
