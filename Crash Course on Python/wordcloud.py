#Please upload any file in jupyter as per #instruction****important: Pls read the #instructions carefully***** 
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can","for","will", "just"]
    
        # LEARNER CODE START HERE
    dict={}
    no_punct=""
    for i in file_contents:
        if i not in punctuations:
            no_punct+=i
    lst=no_punct.split(" ")
    for item in lst:
        if item in uninteresting_words:
            lst.remove(item)
        else:
            for i in range(len(no_punct)):
                dict[item]=i
    
      
        
        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict)
    return cloud.to_array()
# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()