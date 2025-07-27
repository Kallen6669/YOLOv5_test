from torch.utils.data import Dataset, DataLoader
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
        return None


def main():
    image_dir = "/voc_data/train/imgs"
    label_dir = "/voc_data/train/labels"
    dataset = VOCDataset(image_dir, label_dir)
    print(len(dataset))
    print(dataset[0])


if __name__ == "__main__":
    main()