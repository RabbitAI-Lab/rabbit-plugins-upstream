# Denote Top Ads

EN · [ZH](README.zh.md) · [JA](README.ja.md) · [KO](README.ko.md) · [ES](README.es.md) · [NL](README.nl.md) · [DE](README.de.md) · [FR](README.fr.md)

Find winning ads to study for your next campaign. Denote tracks more than 10 million ads and updates its rankings every week. A free account gives you three charts for games or apps from the last completed week, with up to ten creatives per chart. [Explore Denote Top Ads](https://denote.net/top-ads).

![Open the three weekly charts from the Top Ads sidebar.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/top-ads-navigation.jpg)

*Open the three weekly charts from the Top Ads sidebar.*

| Free chart | What it shows |
| --- | --- |
| Trending Ads | See which creatives drew the most attention last week. |
| Rising Ads | Find creatives with the biggest week-over-week gain in popularity. |
| New Ads | Discover newly spotted creatives ranked by early popularity. |

![Trending ads in games for November 9–15, 2026, ranked by weekly popularity.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/trending-ads.jpg)

*Trending ads in games for November 9–15, 2026, ranked by weekly popularity.*

![Rising game ads with the largest week-over-week gains in popularity.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/rising-ads.jpg)

*Rising game ads with the largest week-over-week gains in popularity.*

![Newly spotted game ads ranked by early popularity.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/new-ads.jpg)

*Newly spotted game ads ranked by early popularity.*

## Get your first report

Run this command in your OpenClaw workspace. The skill requires Python 3.

```sh
git clone https://github.com/Denote-Business/denote-top-ads.git skills/denote-top-ads
```

1. Start a new session and ask “What can Denote Top Ads help me find?”
2. [Create a free Denote account](https://denote.net/user/register). Already registered? Sign in. Create a Denote API key with the `top_ads:read` permission or add it to an existing key.
3. Save the key as `DENOTE_API_KEY` in your agent host’s secret settings. Then ask “Show me last week’s top app ads.” Your agent will fetch all three charts. Games are the default when you leave the category open.

**Rank · Ad title · Advertiser · Format · Platforms · Preview**

## A closer look

Ask “Open the second ad on the rising chart.” Top Ads Pro or Business includes available creative details such as performance and audience. All three weekly charts are free.

![Overview of the Vita Mahjong creative, including its format and estimated impressions.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/overview.jpg)

*Overview of the Vita Mahjong creative, including its format and estimated impressions.*

![Daily creative score for Vita Mahjong alongside reference lines.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/data-trend.jpg)

*Daily creative score for Vita Mahjong alongside reference lines.*

![Other ads using the Vita Mahjong creative, with advertiser and run dates.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/related-ads.jpg)

*Other ads using the Vita Mahjong creative, with advertiser and run dates.*

![Vita Mahjong audience reach by country, age and gender.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/audience.jpg)

*Vita Mahjong audience reach by country, age and gender.*
