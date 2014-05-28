# md2db

Python script to convert peculiarly formatted Markdown file into SQLite-compatible database.

## Example input file

```Markdown
### 31.12.15 - 13:37

> It's a trap!

Source: [Admiral Ackbar, _Star Wars_](http://www.imdb.com/title/tt0086190/quotes)


### 20.04.14 - 10:07

> "The first rule of any game is to know you're in one." So true.
>
> I would add that the second rule to any game is to know the game is broader than what it seems. Poker is really not just about cards. Startups aren't about building a product. Passing an exam isn't about knowing the answers. Thinking about the broader game opens so much more opportunity than being stuck in what people believe is the game's limit.

Source: [Hacker News comment by _d0m_](https://news.ycombinator.com/item?id=6743647)


### 11.11.11 - 18:27

The very first post here.
```
