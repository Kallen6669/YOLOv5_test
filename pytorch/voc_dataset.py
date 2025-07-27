from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os


class VOCDataset(Dataset):
    def __init__(self, image_dir, label_dir, transform=None, label_transform=None, is_test=False):
        super().__init__()
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.transform = transform
        self.label_transform = label_transform
        self.is_test = is_test
        self.image_list = os.listdir(image_dir)
        self.label_list = os.listdir(label_dir)
        
    def __len__(self):
        return len(self.image_list)
    
    def __getitem__(self, idx):
        image_path = os.path.join(self.image_dir, self.image_list[idx])
        label_path = os.path.join(self.label_dir, self.label_list[idx])
        image = Image.open(image_path).convert("RGB")
        label = Image.open(label_path).convert("L")
        return image, label


def main():
    image_dir = "/voc_data/train/imgs"
    label_dir = "/voc_data/train/labels"
    dataset = VOCDataset(image_dir, label_dir)
    print(len(dataset))
    print(dataset[0])


if __name__ == "__main__":
    main()