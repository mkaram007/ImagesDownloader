from Download import download_images


def main():
    try:
        download_images()
    except Exception as e:
        print("An error occured, please consult the developer\n", e)
        main()

if __name__ == '__main__':
    main()
