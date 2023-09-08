from pathlib import Path 

def get_paths_labels(args):
    paths = {cls: [] for cls in args.classes}   # Get image path in first list and label paht in second paths
    for c in args.classes:
        imgs = sorted(list(Path(args.data).glob(f"{c}/*.jpg")))
        labels = sorted(list(Path(args.data).glob(f"{c}/*.json")))
        paths[c] += [(img, label) for img, label in zip(imgs, labels)]
    return paths