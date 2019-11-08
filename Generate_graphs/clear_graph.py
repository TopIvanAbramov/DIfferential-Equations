from PIL import Image

def clear(): #function clear graphs (interface)
    img = Image.new('RGB', (800, 800), (255, 255, 255))
    img.save("Graphs/solution.png", "PNG")
