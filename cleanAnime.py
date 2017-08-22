import os

thisSeason = "/run/media/renge/Gamma/Anime/This Season"
for folders in os.listdir(thisSeason):
        folderPath = os.path.join(thisSeason, folders)
        for animeFile in os.listdir(folderPath):
            allFiles = dict(title = animeFile[0])

print(allFiles)
