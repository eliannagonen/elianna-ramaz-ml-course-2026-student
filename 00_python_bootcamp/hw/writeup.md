# HW00 Writeup — Song Analysis

Run `uv run python analysis.py` to generate the results, then answer the five questions
below. Replace each `[your answer here]` with your response.

- Questions 1–3 are factual. One or two sentences is enough.
- Question 4 asks you to reflect on something that surprised you.
- Question 5 asks you to connect what you implemented in Part 1 to the two new tools from Part 2.

---

## Question 1 (2 pts)

**Which genre averaged the most weeks on the Billboard chart, and how many
songs is that average computed from?**

Afrobeats with 30 weeks from 1 song.

---

## Question 2 (2 pts)

**Who was the most-streamed artist in the dataset (by total streams across all their songs)?**

Taylor Swift with 6560M total streams. 

---

## Question 3 (2 pts)

**Which year had the most top-10 hits (songs that peaked at position 10 or better)?**

2024 with 26 hits.

---

## Question 4 (4 pts)

**What surprised you about the data?**

Pick one finding from your analysis that was unexpected — something that contradicts what
you assumed going in, or that is more interesting than you expected. Explain:
- What you expected to see, and why.
- What the data actually showed.
- What might explain the difference.

I expected the number of top-10 hits per year to be roughly similar, but I was surprised to see that there was a big jump in 2024 with 26 top-10 hits, compared to every other year in the dataset with 10-16. 2024 might stand out because the songs are newer, so they haven't been pushed out of the top 10 yet by later competition. Songs from older years had more time to fall down in rankings. 

---

## Question 5 (5 pts)

In Part 1 you implemented `count_occurrences` from scratch using only a plain Python
dict. `collections.Counter`, which you used in Part 2, does the same thing but with
extra conveniences built in.

Answer both parts:

**a)** Walk through, step by step, how you accumulated a running total per genre/artist
in `avg_weeks_by_genre` and `most_streamed_artist`, and how you determined the maximum
in `most_streamed_artist`. Would `collections.Counter` have made any part of this
easier, and if so, which part (drawing on how you'd extend your own `count_occurrences`
to do the same thing)?

**b)** `StreamsRanker` and `LongevityRanker` both subclass `SongRanker` and share its
`rank` method, overriding only `score`. If they did **not** share a common base class —
if you had written two separate, unrelated classes instead — what code would you have
had to duplicate? What does inheritance buy you here?


a) For both 'avg_weeks_by_genre' and 'most_streamed_artist', I used the same pattern to accumulate a running total. I initialized an empty dictionary before the loop, then for each item checked if the key (genre or artist) already existed in the dictionary. If it did, I added to the existing total; if not, I initialized it to the current value. For genres, I actually kept two running totals: 'weeks_by_genre' for the sum of weeks on chart, and 'songs_by_genre' for the count of songs, since I needed both to compute an average (total weeks/number of songs).

To find the max in 'most_streamed_artist', I looped through streams_by_artist' and kept two variables: 'top_artist' and 'top_streams', both starting at None. On each artist, I checked if 'top_streams' was still None (for the first case where no artist had been compared yet) or if the current artist's stream count was greater than 'top_streams'. If either was true, I updated both 'top_artist' and top_streams' to the current artist and their count. By the end of the loop, 'top_artist' held the name of the artist with the highest total streams.

In 'count_occurences', Counter(items) could have replaced the entire if statement. Counter(s["genre"] for s in songs) replaces the 'songs_by_genre' accumulation logic in 'avg_weeks_by_genre', since it gives you a dict mapping each genre to how many songs belong to it. 

b) If 'StreamsRanker' and 'LongevityRanker' didn't share a common base class, I would have has to duplicate the entire 'rank()' method, word for word, in both classes (even though it never references anything class specific - only 'self.score' which resolves to whichever class's score is defined). The only thing that would actually need to be different between the two classes is the single line inside 'score()' for which dict key gets returned. Inheritance is helpful because if I ever found a bug in 'rank()', I'd only need to fix it in one place instead of in every duplicate. Also, if I wanted to add a third ranker, I'd only need to write 'score()' because rank() would automatically transfer to another subclass. 