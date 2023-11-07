import argparse
from PIL import Image
import io

def compress_image_to_target_size_and_save(image_path, target_size_kb, output_path, quality_step=5):
    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    quality = 100
    while True:
        img_file = io.BytesIO()
        img.save(img_file, format='JPEG', quality=quality)
        img_size_kb = img_file.tell() / 1024
        
        if img_size_kb <= target_size_kb or quality <= 10:
            with open(output_path, 'wb') as f:
                f.write(img_file.getvalue())
            break
        
        quality -= quality_step
    
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Compress an image to a specified size.')
    parser.add_argument('image_path', type=str, help='The path to the image to be compressed.')
    parser.add_argument('target_size_kb', type=int, help='The desired target size in kilobytes.')
    args = parser.parse_args()

    output_path = args.image_path.rsplit('.', 1)[0] + '_compressed.jpg'
    compress_image_to_target_size_and_save(args.image_path, args.target_size_kb, output_path)

if __name__ == '__main__':
    main()
