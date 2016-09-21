import pickle
from LanguageModel import LanguageModel


model = LanguageModel("subtitles")
pickle.dump(model,open("model.p","wb"))