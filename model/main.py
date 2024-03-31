import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-output_dir', type=str, default=None, help="Path to the output directory.")

    opt = parser.parse_args()

    if opt.output_dir is not None:
        print(opt.output_dir)

if __name__ == "__main__":
    main()