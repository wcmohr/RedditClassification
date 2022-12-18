def clean_data(reference_or_latest):
    ``` ```    
    if reference_or_latest == 'reference':
        fpath = './scitech_data_scraped/scitech_data_\
                2022:12:17:08:31:221671294682.879364.csv'
    else:
        fpath = max(glob.glob('./scitech_data_scraped/*.csv'), key=os.path.getctime)
        
    sci_tech_data = pd.read_csv(fpath)
    
    #Below I select the relevent rows that have tech or science as the subreddits and save the feature space, 'title' and the target, 'subreddit' to respective variables.
    
    subreddit = sci_tech_data.loc[(sci_tech_data['subreddit'].isin(
                                ['technology','science']), 'subreddit')]
    title = sci_tech_data.loc[(sci_tech_data['subreddit'].isin(
                                ['technology','science']),'title')]
    
    X = title
    y = subreddit
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)
    
#     [source: strip characters from string in series](https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column)
# [source: remove punctuation](https://www.google.com/search?q=how+to+replace+punctuation+with+regular+expression+python&rlz=1C5CHFA_enUS983US983&oq=how+to+replace+punctuation+with+regular&aqs=chrome.1.69i57j33i160l2.10574j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_7SabY4OANaSs0PEP042roAM_32)
    for r in remove_group:
# replace hyphens with space, then remove emojis, punctuation, digits, and urls
    X_train_filtered = X_train.map(lambda x: clean(
                                re.sub('-',repl=' ', string = x) , no_emoji=True,
                                    no_punct=True,no_digits=True, no_urls=True))
    
    X_train_filtered = X_train_filtered.map(lambda x: re.sub('(0|\|)',
                                                        repl='',string = x))
print((sum([len(s) for s in X_train])-sum([len(s) for s in X_train_filtered]))
    /sum([len(s) for s in X_train])
)


# I'll keep (<url>) group in the words, in case there is differential frequency