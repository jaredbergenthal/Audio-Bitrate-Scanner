







# import os
# import tkinter as tk
# from tkinter import filedialog
# from mutagen.mp3 import MP3
#
# # Create a Tkinter GUI window
# root = tk.Tk()
# root.withdraw()
#
# # Ask the user to select a folder
# folder_path = filedialog.askdirectory()
#
# # Scan through all .mp3 files in the root folder and write to 'Audio Results.txt'
# results_file_path = os.path.join(folder_path, 'Audio Results.txt')
# with open(results_file_path, 'w') as results_file:
#     for filename in os.listdir(folder_path):
#         if os.path.splitext(filename)[1].lower() == '.mp3':
#             # Get the full path of the file
#             file_path = os.path.join(folder_path, filename)
#
#             # Get the bitrate of the file using the mutagen module
#             audio = MP3(file_path)
#             bitrate = audio.info.bitrate // 1000
#
#             # Write the filename and bitrate to the 'Audio Results' text file
#             results_file.write(filename + ': ' + str(bitrate) + 'kbps\n')
#
# # Scan through all subdirectories and write to separate 'Audio Results.txt' files
# for root_folder, subfolders, files in os.walk(folder_path):
#     for subfolder in subfolders:
#         subfolder_path = os.path.join(root_folder, subfolder)
#         results_file_path = os.path.join(subfolder_path, 'Audio Results.txt')
#         with open(results_file_path, 'w') as results_file:
#             for filename in os.listdir(subfolder_path):
#                 if os.path.splitext(filename)[1].lower() == '.mp3':
#                     # Get the full path of the file
#                     file_path = os.path.join(subfolder_path, filename)
#
#                     # Get the bitrate of the file using the mutagen module
#                     audio = MP3(file_path)
#                     bitrate = audio.info.bitrate // 1000
#
#                     # Write the filename and bitrate to the 'Audio Results' text file
#                     results_file.write(filename + ': ' + str(bitrate) + 'kbps\n')
#
# # Notify the user that the program has finished
# print('Done!')

# def Bitrate_Finder():
#     import os
#     import tkinter as tk
#     from tkinter import filedialog
#     from mutagen.mp3 import MP3
#
#     # Create a Tkinter GUI window
#     root = tk.Tk()
#     root.withdraw()
#
#     # Ask the user to select a folder
#     folder_path = filedialog.askdirectory()
#
#     # Scan through all .mp3 files in the root folder and write to 'Ω Audio Results.txt'
#     results_file_path = os.path.join(folder_path, 'Ω Audio Results.txt')
#     with open(results_file_path, 'w') as results_file:
#         for filename in os.listdir(folder_path):
#             if os.path.splitext(filename)[1].lower() == '.mp3':
#                 # Get the full path of the file
#                 file_path = os.path.join(folder_path, filename)
#
#                 # Get the bitrate of the file using the mutagen module
#                 audio = MP3(file_path)
#                 bitrate = audio.info.bitrate // 1000
#
#                 # Write the filename and bitrate to the 'Ω Audio Results' text file
#                 results_file.write(filename + ': ' + str(bitrate) + 'kbps\n')
#
#     # Scan through all subdirectories and write to separate 'Ω Audio Results.txt' files
#     for root_folder, subfolders, files in os.walk(folder_path):
#         for subfolder in subfolders:
#             subfolder_path = os.path.join(root_folder, subfolder)
#             results_file_path = os.path.join(subfolder_path, 'Ω Audio Results.txt')
#             if not os.path.exists(results_file_path):
#                 with open(results_file_path, 'w') as results_file:
#                     for filename in os.listdir(subfolder_path):
#                         if os.path.splitext(filename)[1].lower() == '.mp3':
#                             # Get the full path of the file
#                             file_path = os.path.join(subfolder_path, filename)
#
#                             # Get the bitrate of the file using the mutagen module
#                             audio = MP3(file_path)
#                             bitrate = audio.info.bitrate // 1000
#
#                             # Write the filename and bitrate to the 'Ω Audio Results' text file
#                             results_file.write(filename + ': ' + str(bitrate) + 'kbps\n')
#
#     # Notify the user that the program has finished
#     print('Done!')


def Bitrate_Finder_Remover():
    import os
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    folder_selected = filedialog.askdirectory()

    for subdir, dirs, files in os.walk(folder_selected):
        for file in files:
            if file == 'Ω Audio Results.txt':
                os.remove(os.path.join(subdir, file))




def Bitrate_Finder():
    import os
    import tkinter as tk
    from tkinter import filedialog
    from mutagen.mp3 import MP3
    from mutagen.mp4 import MP4

    # Create a Tkinter GUI window
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory()

    # Initialize a variable to keep track of whether there are .mp3 or .m4a files in the root folder
    root_has_audio_files = False

    # Scan through all .mp3 and .m4a files in the root folder and write to 'Ω Audio Results.txt'
    results_file_path = os.path.join(folder_path, 'Ω Audio Results.txt')
    for filename in os.listdir(folder_path):
        if os.path.splitext(filename)[1].lower() in ['.mp3', '.m4a']:
            root_has_audio_files = True
            break

    if root_has_audio_files:
        with open(results_file_path, 'w', encoding='utf-8') as results_file:
            for filename in os.listdir(folder_path):
                if os.path.splitext(filename)[1].lower() in ['.mp3', '.m4a']:
                    # Get the full path of the file
                    file_path = os.path.join(folder_path, filename)

                    # Get the bitrate of the file using the mutagen module
                    if os.path.splitext(filename)[1].lower() == '.mp3':
                        audio = MP3(file_path)
                    else:
                        audio = MP4(file_path)
                    bitrate = audio.info.bitrate // 1000

                    # Write the filename and bitrate to the 'Ω Audio Results' text file
                    results_file.write(filename + ': ' + str(bitrate) + 'kbps\n')

    # Scan through all subdirectories and write to separate 'Ω Audio Results.txt' files
    for root_folder, subfolders, files in os.walk(folder_path):
        for subfolder in subfolders:
            subfolder_path = os.path.join(root_folder, subfolder)
            results_file_path = os.path.join(subfolder_path, 'Ω Audio Results.txt')
            with open(results_file_path, 'w') as results_file:
                for filename in os.listdir(subfolder_path):
                    if os.path.splitext(filename)[1].lower() in ['.mp3', '.m4a']:
                        # Get the full path of the file
                        file_path = os.path.join(subfolder_path, filename)

                        # Get the bitrate of the file using the mutagen module
                        if os.path.splitext(filename)[1].lower() == '.mp3':
                            audio = MP3(file_path)
                        else:
                            audio = MP4(file_path)
                        bitrate = audio.info.bitrate // 1000

                        # Write the filename and bitrate to the 'Ω Audio Results' text file
                        results_file.write(filename + ': ' + str(bitrate) + 'kbps\n')

    # Notify the user that the program has finished
    print('Done!')


Bitrate_Finder()




