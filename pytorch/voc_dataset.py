from torch.utils.data import Dataset, DataLoader
import torch
from torchvision import transforms
from PIL import Image
import os
import xmltodict


class VOCDataset(Dataset):
    def __init__(self, image_dir, label_dir,class_dir, transform=None, label_transform=None, is_test=False):
        super().__init__()
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.transform = transform
        self.label_transform = label_transform
        self.is_test = is_test
        self.image_list = os.listdir(image_dir)
        self.label_list = os.listdir(label_dir)
        with open(class_dir, "r") as f:
            self.classes = f.read().splitlines()
        
    def __len__(self):
        return len(self.image_list)
    
    def __getitem__(self, idx):
        image_path = os.path.join(self.image_dir, self.image_list[idx])
        label_path = os.path.join(self.label_dir, self.label_list[idx])
        image = Image.open(image_path).convert("RGB")
        if self.transform is not None:
            image = self.transform(image)
        with open(label_path, "r") as f:
            label_dict = xmltodict.parse(f.read())
        label = [];
        label_signal = []
        for obj in label_dict["annotation"]["object"]:
            label_signal = []
            label_signal.append(self.classes.index(obj["name"]))
            label_signal.append(obj["bndbox"]["xmin"])
            label_signal.append(obj["bndbox"]["ymin"])
            label_signal.append(obj["bndbox"]["xmax"])
            label_signal.append(obj["bndbox"]["ymax"])
            label.append(label_signal)
        return image, label


def main():
    image_dir = "voc_data/train/imgs"
    label_dir = "voc_data/train/labels"
    class_dir = "voc_data/train/classes"
    transform = transforms.Compose([
        transforms.ToTensor()
    ])
    dataset = VOCDataset(image_dir, label_dir, class_dir, transform=transform)
    dataloader = DataLoader(dataset, batch_size=4, shuffle=True, num_workers=4)
    for idx, (images, labels) in enumerate(dataloader):
        print(images.shape)
        print(labels)


if __name__ == "__main__":
    main()