import pandas as pd
import contextily as cx
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import math

# ==========================================
# CONFIGURATION
# ==========================================
TRAIN_PATH =r"data\raw\train(1).xlsx"
TEST_PATH = r"data\raw\test2.xlsx"
OUTPUT_DIR =r"data\images"
ZOOM_LEVEL = 18 

# Add this helper function at the top of your script
def latlon_to_wm(lat, lon):
    """Converts Latitude/Longitude to Web Mercator coordinates."""
    x = lon * 20037508.34 / 180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * 20037508.34 / 180
    return x, y

def download_house_image(lat, lon, house_id, output_folder):
    filename = f"{house_id}.jpg"
    filepath = os.path.join(output_folder, filename)
    
    if os.path.exists(filepath):
        return
    
    try:
        # Manually calculate the bounding box in Web Mercator
        # 0.0006 is roughly the offset for a single house view
        cx_wm, cy_wm = latlon_to_wm(lat, lon)
        offset = 150  # meters
        
        west, east = cx_wm - offset, cx_wm + offset
        south, north = cy_wm - offset, cy_wm + offset
        
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_xlim(west, east)
        ax.set_ylim(south, north)
        
        # Add the Esri Satellite imagery
        cx.add_basemap(ax, source=cx.providers.Esri.WorldImagery, zoom=18)
        
        ax.set_axis_off()
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)
        
        plt.savefig(filepath, dpi=100, bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        
    except Exception as e:
        print(f"Error for {house_id}: {e}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Loading data...")
    df_train = pd.read_excel(TRAIN_PATH)
    df_test = pd.read_excel(TEST_PATH)
    df = pd.concat([df_train[['id', 'lat', 'long']], df_test[['id', 'lat', 'long']]])

    # FOR TESTING: Just do the first 50 images to make sure it works
    # After testing, remove the '.head(50)' to do the whole dataset
    print("Starting download...")
    for _, row in tqdm(df.head(100).iterrows(), total=100):
        download_house_image(row['lat'], row['long'], int(row['id']), OUTPUT_DIR)

if __name__ == "__main__":
    main()