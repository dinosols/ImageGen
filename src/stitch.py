import sys
from PIL import Image
import argparse
from os import listdir
from os import path
import itertools
from random import randrange, choice, choices
import string

def stitch(output_dir, *img_args):
    newImage = Image.new('RGBA', (1500, 1500))
    #name = "".join(choices(string.ascii_letters, k=5)) + "_"
    name = "_"
    for imagePath in img_args:
        if imagePath != None:
            basename = path.basename(imagePath)
            fname = path.splitext(basename)[0]
            name += str(fname) + "_"
            img = Image.open(imagePath)
            if img.mode == "RGB":
                img = img.convert("RGBA")
            newImage.alpha_composite(img.resize((1500, 1500)))
        else:
            name += str(None) + "_"
    newImage.save(output_dir + name + ".png")

parser = argparse.ArgumentParser()
parser.add_argument("backgrounds", help="The directory of background images.")
parser.add_argument("dinos", help="The directory of dinosaur images.")
parser.add_argument("traits", help="The directory of trait images.")
parser.add_argument("texture", help="The texture to add to the image last.")
parser.add_argument("output", help="The directory to save generated images to.")
args = parser.parse_args()
print(args)

backgrounds = listdir(args.backgrounds)
print("Backgrounds: " + str(backgrounds))
dinos = listdir(args.dinos)
print("Dinos: " + str(dinos))
traits = listdir(args.traits)
print("Trait types: " + str(traits))
traitMap = {}
for trait in traits:
    traitMap[trait] = listdir(args.traits + trait)
    traitMap[trait].append(None)
for key in traitMap.keys():
    print("\t" + key + ": " + str(traitMap[key]))

allTraitPaths = []
for traitType in traits:
    traitList = []
    for trait in traitMap[traitType]:
        if trait != None:
            traitList.append(args.traits + traitType + "/" + trait)
        else:
            traitList.append(None)
    allTraitPaths.append(traitList)

traitPathCombos = list(itertools.product(*allTraitPaths))

for background in backgrounds:
    for dino in dinos:
        for traitCombo in traitPathCombos:
            bgPath = args.backgrounds + background
            dinoPath = args.dinos + dino
            #if randrange(20000) == 0:
            stitch(args.output, bgPath, dinoPath, *traitCombo, args.texture)



