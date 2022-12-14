import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    
    total = sum(ranks.values())
    print(f"The sum of all probability of Sampling Results: {total}\n")

    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    total = sum(ranks.values())
    print(f"The sum of all probability of Iteration Results: {total}\n")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Probability distribution
    PrB = {}

    # List of pages linked to the current page
    linked_pgs = corpus[page]

    # If the page has no links, return a probability distribution
    # that chooses randomly among all pages with equal probability
    if not linked_pgs:
        for link in corpus:
            PrB[link] = 1 / len(corpus)
    else:
        # Calculate the probability of choosing a random link from the current page
        prob_random_link = damping_factor / len(linked_pgs)

        # Calculate the probability of choosing a random page from the corpus
        prob_random_page = (1 - damping_factor) / len(corpus)

        # Calculate the probability of visiting each page in the corpus
        for link in corpus:
            if link in corpus[page]:
                PrB[link] = prob_random_link
            else:
                PrB[link] = prob_random_page

    return PrB

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    # Initialize PageRank
    PageRank = {page: 0 for page in corpus}

    # Choose a random page
    sample = random.choice(list(corpus.keys()))

    # Sample n pages according to transition model
    for _ in range(n-1):
        PageRank[sample] += 1
        PrB = transition_model(corpus, sample, damping_factor)
        sample = random.choices(list(PrB.keys()), PrB.values())[0]

    # Normalize the PageRank values to sum to 1
    sum_values = sum(PageRank.values())
    for page in PageRank:
        PageRank[page] /= sum_values

    return PageRank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Initialize PageRank to a uniform distribution
    PageRank = {page: 1 / len(corpus) for page in corpus}
    
    while True:
        # Store the new PageRank values
        previous_PageRank = PageRank.copy()
        
        #Calculate the new PageRank values
        for page in corpus:
            sum_previous_PageRank = 0
            
            # Calculate the sum of the previous PageRank values
            # of the pages that link to the current page
            for link in corpus:
                if page in corpus[link]:
                    sum_previous_PageRank += previous_PageRank[link]/len(corpus[link])
                # If the current link page has no links, add the previous PageRank value of the link page
                # divided by the number of pages in the corpus
                if len(corpus[link]) == 0:
                    sum_previous_PageRank += (previous_PageRank[link])/len(corpus)
            PageRank[page] = (1-damping_factor) / len(corpus) + damping_factor * sum_previous_PageRank
        
        # Check for convergence
        dif = abs(PageRank[page] - previous_PageRank[page])
        if dif < 0.001:
            break
        
    return PageRank


if __name__ == "__main__":
    main()