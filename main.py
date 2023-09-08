
import argparse 
from pathlib import Path 
import random 
import shutil
from tqdm import tqdm 
from utils import text_or_none, get_paths_labels

def main(args):
    # Set random seed 
    random.seed(21)

    # Read images using path    
    paths = get_paths_labels(args)
    
    # Get number of cycle 
    n_cycle = len(paths[args.classes[0]]) // args.n_hil if len(paths[args.classes[0]]) % args.n_hil == 0 else (len(paths[args.classes[0]]) // args.n_hil) + 1

    # Get data per cycle 
    for n in tqdm(range(n_cycle)):
        for cls, img_label_list in paths.items():
            sampled = random.sample(img_label_list, args.n_hil)
            paths[cls] = list(set(paths[cls]) - set(sampled))
            save_path = Path(args.save_path) / f"{n}" / cls
            save_path.mkdir(parents=True, exist_ok=True)

            for img_p, label_p in sampled: 
                shutil.copy(img_p, save_path)
                if args.label_save:
                    shutil.copy(label_p, save_path) 


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data",
                        type=str,
                        required=True,
                        help="The path to the folder containing the data you want to split")
    parser.add_argument("--n_hil",
                        type=int,
                        required=False,
                        default=20,
                        help="number of data per HIL cycle")
    parser.add_argument("--classes",
                        type=text_or_none,
                        nargs="+",
                        default=None,
                        help="data's class names")
    parser.add_argument("--save_path",
                        type=str,
                        default="result/",
                        help="Folder that results are saved")
    parser.add_argument("--label_save",
                        type=bool,
                        default=True,
                        help="Decide whether to save labels as well when saving HIL folders")
    args = parser.parse_args()

    main(args)


