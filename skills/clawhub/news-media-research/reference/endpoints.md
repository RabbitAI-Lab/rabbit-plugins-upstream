# news-media-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**80 endpoints across 16 platform group(s).**

## Al Jazeera (5)

### `aljazeera_article`

- **HTTP:** `GET /aljazeera/article`
- **What:** Get Al Jazeera article content. Returns a public Al Jazeera article's metadata and body paragraphs from a canonical article URL.
- **Params:** `url` (string, **required**) — Canonical www.aljazeera.com article URL

### `aljazeera_author`

- **HTTP:** `GET /aljazeera/author`
- **What:** Get an Al Jazeera author's profile and recent articles. Returns one Al Jazeera author's public profile (name, job title, bio when available) and one page of their recent articles, identified by an author slug or a canonical author URL.
- **Params:** `page` (integer, optional) — 1-based page number of the author's article list; overrides any page embedded in url; `slug` (string, optional) — Al Jazeera author slug; `url` (string, optional) — Canonical https://www.aljazeera.com/author/<slug> URL, as an alternative to slug

### `aljazeera_categories`

- **HTTP:** `GET /aljazeera/categories`
- **What:** Get Al Jazeera section navigation. Returns Al Jazeera's current public section navigation. Use a returned slug directly as the topic parameter on aljazeera-topic.
- **Params:** _none_

### `aljazeera_headlines`

- **HTTP:** `GET /aljazeera/headlines`
- **What:** Get Al Jazeera site-wide headlines. Returns fresh headlines from Al Jazeera's public, site-wide RSS feed.
- **Params:** _none_

### `aljazeera_topic`

- **HTTP:** `GET /aljazeera/topic`
- **What:** Get Al Jazeera section headlines. Returns the newest public Al Jazeera stories from one section archive page. topic is a section slug; use aljazeera-categories for the current value space.
- **Params:** `topic` (string, **required**) — Al Jazeera section slug

## Axios (3)

### `axios_article`

- **HTTP:** `GET /axios/article`
- **What:** Get Axios article content. Returns a public Axios article's metadata and full body paragraphs from a canonical article URL. Subscriber-only stories with no free preview return a 403 permission error instead of an empty body.
- **Params:** `url` (string, **required**) — Canonical www.axios.com article URL

### `axios_categories`

- **HTTP:** `GET /axios/categories`
- **What:** Get Axios topic navigation. Returns Axios's full public topic and subtopic navigation tree. Use a subtopic's topic value directly as the topic parameter on axios-headlines.
- **Params:** _none_

### `axios_headlines`

- **HTTP:** `GET /axios/headlines`
- **What:** Get Axios topic headlines. Returns the newest public Axios stories on one topic or subtopic page. topic is a topic slug (e.g. technology) or a topic/subtopic path (e.g. technology/automation-and-ai) -- see axios-categories for the full known value space.
- **Params:** `topic` (string, **required**) — Axios topic slug or topic/subtopic path

## BBC (5)

### `bbc_article`

- **HTTP:** `GET /bbc/article`
- **What:** Get BBC News article content. Returns a BBC News article's public metadata and body paragraphs from a canonical article URL. Live pages are not supported.
- **Params:** `url` (string, **required**) — Canonical BBC News article URL

### `bbc_author`

- **HTTP:** `GET /bbc/author`
- **What:** Get a BBC News correspondent's profile. Returns a BBC News correspondent's public profile: name, short bio, and their recent articles.
- **Params:** `url` (string, **required**) — Canonical BBC News correspondent URL

### `bbc_headlines`

- **HTTP:** `GET /bbc/headlines`
- **What:** Get BBC News section headlines. Returns fresh headlines from a public BBC News RSS section. section defaults to world.
- **Params:** `section` (string, optional) — BBC News RSS section, defaults to world

### `bbc_live`

- **HTTP:** `GET /bbc/live`
- **What:** Get a BBC News live-page text snapshot. Returns the current server-rendered text updates from one canonical BBC News live URL. It does not subscribe to updates or return broadcast, player, or stream data.
- **Params:** `url` (string, **required**) — Canonical BBC News live URL

### `bbc_search`

- **HTTP:** `GET /bbc/search`
- **What:** Search public BBC pages. Returns a bounded page of public BBC search-result metadata: title, URL, standfirst summary, display date, and a type of article, video, audio, live, topic, or page. Topic items are BBC topic hub pages rather than articles and carry no published_at. Media entries link only to their BBC landing pages; streams, downloads, and transcripts are not returned.
- **Params:** `page` (integer, optional) — Results page, defaults to 1; `q` (string, **required**) — Search query, up to 120 characters

## Bloomberg (6)

### `bloomberg_article`

- **HTTP:** `GET /bloomberg/article`
- **What:** Get a Bloomberg article's content. Returns one public Bloomberg article's metadata and body paragraphs from a canonical article URL. Subscriber-only articles are not available.
- **Params:** `url` (string, **required**) — Canonical Bloomberg article URL

### `bloomberg_author`

- **HTTP:** `GET /bloomberg/author`
- **What:** Get a Bloomberg author's profile. Returns one public Bloomberg author's profile (name, title, bio) and their recent-content feed from a canonical author URL.
- **Params:** `url` (string, **required**) — Canonical Bloomberg author URL

### `bloomberg_categories`

- **HTTP:** `GET /bloomberg/categories`
- **What:** List Bloomberg editorial categories. Lists Bloomberg's public editorial navigation categories discovered from its embedded navigation state. Each returned section slug is accepted by /bloomberg/headlines; product, account, newsletter, and sponsored-content links are excluded.
- **Params:** _none_

### `bloomberg_headlines`

- **HTTP:** `GET /bloomberg/headlines`
- **What:** Get the latest stories in a Bloomberg section. Returns Bloomberg story cards from one editorial section. Section must be a slug returned by /bloomberg/categories.
- **Params:** `section` (string, **required**) — Section slug from /bloomberg/categories

### `bloomberg_news`

- **HTTP:** `GET /bloomberg/news`
- **What:** Get the latest Bloomberg stories. Returns Bloomberg's current news feed: the newest stories across all sections, each with its title, canonical URL, and publication time.
- **Params:** _none_

### `bloomberg_news_sitemaps`

- **HTTP:** `GET /bloomberg/news-sitemaps`
- **What:** List Bloomberg monthly news sitemaps. Returns Bloomberg's public monthly news-sitemap index so callers can discover historical news feeds beyond the rolling latest feed.
- **Params:** _none_

## CNN (4)

### `cnn_article`

- **HTTP:** `GET /cnn/article`
- **What:** CNN article content. Returns a CNN article's headline, description, author, publication and update times, section, image, and body paragraphs. Provide a canonical cnn.com article URL.
- **Params:** `url` (string, **required**) — Canonical cnn.com article URL

### `cnn_author`

- **HTTP:** `GET /cnn/author`
- **What:** CNN profile page. Returns one CNN profile's byline metadata (name and title), bio paragraphs, social accounts, and recent articles/videos. Provide either a profile slug or a canonical cnn.com/profiles/<slug> URL.
- **Params:** `slug` (string, optional) — CNN profile slug, e.g. jake-tapper-profile (a slug without the -profile suffix is tried with it first, then as-is); `url` (string, optional) — Canonical cnn.com/profiles/<slug> URL, as an alternative to slug

### `cnn_headlines`

- **HTTP:** `GET /cnn/headlines`
- **What:** CNN section headlines. Returns the current CNN headline stream for one section, including title, article URL, description, publication time, and image when available.
- **Params:** `section` (string, optional) — CNN section. Allowed values: world, us, politics, business, health, entertainment, style, travel, sports, science, climate, weather, opinion. Default world.

### `cnn_live_story`

- **HTTP:** `GET /cnn/live-story`
- **What:** CNN live story updates. Returns a CNN live story's title, description, update time, and chronological post updates. Provide a canonical cnn.com live-news URL.
- **Params:** `url` (string, **required**) — Canonical cnn.com live-news URL

## FT (6)

### `ft_article`

- **HTTP:** `GET /ft/article`
- **What:** Get a Financial Times article's content. Returns one public Financial Times article's metadata and body paragraphs from a canonical article URL. Subscriber-only articles that the FT serves as a subscription page are not available.
- **Params:** `url` (string, **required**) — Canonical FT article URL

### `ft_author`

- **HTTP:** `GET /ft/author`
- **What:** Get an FT author profile. Returns one Financial Times contributor's public byline profile (name, job title, email, social accounts) plus one page of their recent articles. FT author pages carry no bio paragraph, only this byline metadata.
- **Params:** `page` (integer, optional) — 1-based page number of the author's article list; `slug` (string, optional) — Author URL slug, e.g. martin-wolf; `url` (string, optional) — Canonical www.ft.com/<slug> author URL; alternative to slug

### `ft_categories`

- **HTTP:** `GET /ft/categories`
- **What:** List Financial Times sections. Lists every Financial Times section accepted by /ft/headlines, grouped by top-level section, with each section's slug, display name, and landing-page URL.
- **Params:** _none_

### `ft_headlines`

- **HTTP:** `GET /ft/headlines`
- **What:** Get the latest stories in a Financial Times section. Returns one page of a Financial Times section front: each story's title, canonical URL, summary, section tag, publication time, and lead image. Section must be a slug returned by /ft/categories.
- **Params:** `page` (integer, optional) — Results page; `section` (string, **required**) — Section slug from /ft/categories

### `ft_news`

- **HTTP:** `GET /ft/news`
- **What:** Get the latest Financial Times stories. Returns the Financial Times' current news feed: the newest stories across all sections, each with its title, canonical URL, and publication time.
- **Params:** _none_

### `ft_search`

- **HTTP:** `GET /ft/search`
- **What:** Search Financial Times articles. Returns one page of Financial Times search results: each story's title, canonical URL, summary, section tag, publication time, and lead image. Results can be ordered by relevance or date and filtered by publication window.
- **Params:** `date_range` (string, optional) — Publication-window filter; `page` (integer, optional) — Results page; `q` (string, **required**) — Search keywords; `sort` (string, optional) — Result ordering

## ForeignAffairs (5)

### `foreignaffairs_article`

- **HTTP:** `GET /foreignaffairs/article`
- **What:** Extract a Foreign Affairs article. Returns public article metadata and ordered body paragraphs from a canonical Foreign Affairs article URL. Incomplete, truncated, challenge, or contaminated upstream HTML is rejected as an upstream error.
- **Params:** `url` (string, **required**) — Canonical Foreign Affairs article URL

### `foreignaffairs_author`

- **HTTP:** `GET /foreignaffairs/author`
- **What:** Get a Foreign Affairs author profile. Returns one Foreign Affairs contributor's public profile: name, bio, and the recent articles listed on their contributor page. Foreign Affairs does not paginate this page; it shows a fixed recent-article list.
- **Params:** `slug` (string, optional) — Author slug, e.g. robert-kagan; `url` (string, optional) — Canonical foreignaffairs.com/authors/<slug> URL; alternative to slug

### `foreignaffairs_headlines`

- **HTTP:** `GET /foreignaffairs/headlines`
- **What:** Get Foreign Affairs site-wide headlines. Returns fresh Foreign Affairs headlines from the site's public, site-wide RSS feed. Article pages and account state are not required.
- **Params:** _none_

### `foreignaffairs_topic`

- **HTTP:** `GET /foreignaffairs/topic`
- **What:** Get a Foreign Affairs topic feed. Returns the newest items from one Foreign Affairs topic RSS feed. Discover accepted values with foreignaffairs-topics; unknown topic values are rejected before upstream I/O.
- **Params:** `topic` (string, **required**) — Foreign Affairs topic slug from foreignaffairs-topics

### `foreignaffairs_topics`

- **HTTP:** `GET /foreignaffairs/topics`
- **What:** List Foreign Affairs topic feeds. Returns the complete research-backed directory of topic values accepted by foreignaffairs-topic, including each topic's public RSS feed URL.
- **Params:** _none_

## ForeignPolicy (8)

### `foreignpolicy_article`

- **HTTP:** `GET /foreignpolicy/article`
- **What:** Get Foreign Policy article content. Returns a public Foreign Policy article's metadata and full body paragraphs from a canonical article URL. is_gated reports the site's own content-tier marker; the full body is always returned regardless, since Foreign Policy serves it in full to anonymous requests either way.
- **Params:** `url` (string, **required**) — Canonical foreignpolicy.com article URL

### `foreignpolicy_author`

- **HTTP:** `GET /foreignpolicy/author`
- **What:** Get a Foreign Policy author profile. Returns one Foreign Policy contributor's public profile: name, bio, and their recent articles. Further articles load behind a client-side control this endpoint does not follow, so this is the author page's initial recent-article list, not the contributor's full history.
- **Params:** `slug` (string, optional) — Author slug, e.g. anne-applebaum; `url` (string, optional) — Canonical foreignpolicy.com/author/<slug>/ URL; alternative to slug

### `foreignpolicy_headlines`

- **HTTP:** `GET /foreignpolicy/headlines`
- **What:** Get Foreign Policy site-wide headlines. Returns fresh headlines from Foreign Policy's public, site-wide RSS feed. There is no section parameter: use foreignpolicy-topic to scope to one category or tag.
- **Params:** _none_

### `foreignpolicy_live`

- **HTTP:** `GET /foreignpolicy/live`
- **What:** List Foreign Policy Live conversations. Returns Foreign Policy's public FP Live conversation directory. The upstream renders the complete all-conversations list and applies year filtering in the browser.
- **Params:** _none_

### `foreignpolicy_live_detail`

- **HTTP:** `GET /foreignpolicy/live-detail`
- **What:** Get a Foreign Policy Live conversation. Returns one public FP Live conversation by the slug returned by foreignpolicy-live, including its description and any embedded video highlight metadata.
- **Params:** `live` (string, **required**) — Foreign Policy FP Live conversation slug

### `foreignpolicy_project`

- **HTTP:** `GET /foreignpolicy/project`
- **What:** Get a Foreign Policy project hub. Returns a public Foreign Policy curated project hub and its current article cards. Use foreignpolicy-projects to discover live project slugs.
- **Params:** `project` (string, **required**) — Foreign Policy project slug

### `foreignpolicy_projects`

- **HTTP:** `GET /foreignpolicy/projects`
- **What:** List Foreign Policy project hubs. Returns one page of Foreign Policy's live public project directory. Follow next_page until it is zero to enumerate the current project slug space, then pass a slug to foreignpolicy-project.
- **Params:** `page` (integer, optional) — 1-based project-directory page, defaults to 1

### `foreignpolicy_topic`

- **HTTP:** `GET /foreignpolicy/topic`
- **What:** Get Foreign Policy category or tag archive. Returns one page of a public Foreign Policy category or tag archive (newest first). type selects the archive namespace and defaults to category; topic is the slug within it; page is 1-based.
- **Params:** `page` (integer, optional) — 1-based archive page, defaults to 1; `topic` (string, **required**) — Foreign Policy category or tag slug; `type` (string, optional) — Archive namespace, defaults to category

## Guardian (4)

### `guardian_article`

- **HTTP:** `GET /guardian/article`
- **What:** Get Guardian article content. Returns a Guardian article's public metadata and body paragraphs from a canonical article URL. Live-blog timelines are not supported.
- **Params:** `url` (string, **required**) — Canonical www.theguardian.com article URL

### `guardian_author`

- **HTTP:** `GET /guardian/author`
- **What:** Get Guardian contributor profile. Returns one Guardian contributor's public profile: name, bio, Twitter handle, byline image, and one page of their recent articles. Provide either the contributor's profile slug or the full profile page URL.
- **Params:** `page` (integer, optional) — 1-based article-history page, 1 to 100, defaults to 1; `slug` (string, optional) — Guardian contributor profile slug, e.g. hannah-devlin; `url` (string, optional) — Canonical https://www.theguardian.com/profile/<slug> page URL, as an alternative to slug

### `guardian_headlines`

- **HTTP:** `GET /guardian/headlines`
- **What:** Get Guardian section headlines. Returns fresh headlines from a public Guardian RSS section. section defaults to world.
- **Params:** `section` (string, optional) — Guardian RSS section, defaults to world

### `guardian_topic`

- **HTTP:** `GET /guardian/topic`
- **What:** Get Guardian topic archive. Returns the stories on a public Guardian tag archive (20 per page, newest first, with total pages and results) or section front (a single curated page, is_front true). topic is a Guardian tag or section slug and page defaults to 1. resolved_topic reports the path actually served, which differs for edition-scoped fronts.
- **Params:** `page` (integer, optional) — 1-based archive page, 1 to 100, defaults to 1; `topic` (string, **required**) — Guardian tag or section slug

## Harvard Business Review (4)

### `hbr_article`

- **HTTP:** `GET /hbr/article`
- **What:** Get Harvard Business Review article content. Returns a public Harvard Business Review article's metadata and full body text from a canonical article URL. from_magazine flags articles originally published in the print magazine.
- **Params:** `url` (string, **required**) — Canonical hbr.org article URL

### `hbr_categories`

- **HTTP:** `GET /hbr/categories`
- **What:** Get Harvard Business Review topic taxonomy. Returns Harvard Business Review's full public topic taxonomy, grouped into Subject, Industry, and Geography. Use a topic's slug directly as the topic parameter on hbr-topic.
- **Params:** _none_

### `hbr_headlines`

- **HTTP:** `GET /hbr/headlines`
- **What:** Get Harvard Business Review latest headlines. Returns fresh entries from Harvard Business Review's public, site-wide "The Latest" content stream.
- **Params:** _none_

### `hbr_topic`

- **HTTP:** `GET /hbr/topic`
- **What:** Get Harvard Business Review topic archive. Returns the newest public Harvard Business Review articles on one topic archive page. topic is a "<group>/<slug>" value -- see hbr-categories for the full known value space.
- **Params:** `topic` (string, **required**) — Harvard Business Review topic slug

## Los Angeles Times (4)

### `latimes_article`

- **HTTP:** `GET /latimes/article`
- **What:** Get Los Angeles Times article content. Returns a Los Angeles Times article's public metadata and body paragraphs from a canonical article URL, read from the page's NewsArticle structured data.
- **Params:** `url` (string, **required**) — Canonical Los Angeles Times article URL

### `latimes_author`

- **HTTP:** `GET /latimes/author`
- **What:** Get a Los Angeles Times author profile. Returns a Los Angeles Times author's byline metadata, biography, contact/social links, and recent articles from a canonical author URL.
- **Params:** `url` (string, **required**) — Canonical Los Angeles Times author URL

### `latimes_headlines`

- **HTTP:** `GET /latimes/headlines`
- **What:** Get Los Angeles Times section headlines. Returns fresh headlines from a public Los Angeles Times section RSS feed: title, canonical URL, summary, author, publication time, and lead image. section defaults to main.
- **Params:** `section` (string, optional) — Section slug from latimes-sections, defaults to main

### `latimes_sections`

- **HTTP:** `GET /latimes/sections`
- **What:** List Los Angeles Times section feeds. Returns the complete set of section slugs accepted by latimes-headlines, each with its display name and public RSS feed URL.
- **Params:** _none_

## NPR (5)

### `npr_article`

- **HTTP:** `GET /npr/article`
- **What:** Get NPR article content. Returns a public NPR article's metadata and body paragraphs from a canonical article URL.
- **Params:** `url` (string, **required**) — Canonical www.npr.org article URL

### `npr_author`

- **HTTP:** `GET /npr/author`
- **What:** Get an NPR author profile. Returns an NPR author's byline metadata, biography, and recent articles from a canonical author URL.
- **Params:** `url` (string, **required**) — Canonical www.npr.org author URL

### `npr_categories`

- **HTTP:** `GET /npr/categories`
- **What:** Get NPR section navigation. Returns NPR's current public section navigation. Use a returned slug directly as the topic parameter on npr-topic.
- **Params:** _none_

### `npr_headlines`

- **HTTP:** `GET /npr/headlines`
- **What:** Get NPR site-wide headlines. Returns fresh headlines from NPR's public, site-wide RSS feed.
- **Params:** _none_

### `npr_topic`

- **HTTP:** `GET /npr/topic`
- **What:** Get NPR section headlines. Returns the newest public NPR stories from one section archive page. topic is a section slug; use npr-categories for the current value space.
- **Params:** `topic` (string, **required**) — NPR section slug

## New York Times (5)

### `nyt_article`

- **HTTP:** `GET /nyt/article`
- **What:** Get a New York Times article's content. Returns one public New York Times article's metadata and body paragraphs from a canonical article URL.
- **Params:** `url` (string, **required**) — Canonical NYT article URL

### `nyt_author`

- **HTTP:** `GET /nyt/author`
- **What:** Get a New York Times contributor profile. Returns one New York Times contributor's public byline page: name, tagline, About/Contact panels, and their recent articles from a canonical author URL.
- **Params:** `url` (string, **required**) — Canonical NYT author URL

### `nyt_categories`

- **HTTP:** `GET /nyt/categories`
- **What:** List New York Times navigation categories. Lists the public New York Times editorial navigation taxonomy, including top-level categories and nested destinations. Use /nyt/sections for the separately verified RSS-backed section values accepted by /nyt/headlines; product links, newsletters, and podcasts are not included as article categories.
- **Params:** _none_

### `nyt_headlines`

- **HTTP:** `GET /nyt/headlines`
- **What:** Get the latest stories in a New York Times section. Returns a New York Times section RSS feed: each story's title, canonical URL, description, author, publication time, and lead image. Section must be a slug returned by /nyt/sections.
- **Params:** `section` (string, **required**) — Section slug from /nyt/sections

### `nyt_sections`

- **HTTP:** `GET /nyt/sections`
- **What:** List New York Times sections. Lists every New York Times section accepted by /nyt/headlines, with its slug, display name, and public feed URL.
- **Params:** _none_

## Politico (5)

### `politico_article`

- **HTTP:** `GET /politico/article`
- **What:** Get Politico article content. Returns a public Politico article's metadata and full body paragraphs from a canonical article URL.
- **Params:** `url` (string, **required**) — Canonical www.politico.com article URL

### `politico_author`

- **HTTP:** `GET /politico/author`
- **What:** Get a Politico staff author profile. Returns one Politico staff author's public profile: name, job title, bio, headshot, and their most recent bylined articles. Politico staff pages expose a fixed-size recent-articles list with no pagination.
- **Params:** `slug` (string, optional) — Politico staff slug, e.g. mark-satter; `url` (string, optional) — Canonical www.politico.com/staff/<slug> URL, as an alternative to slug

### `politico_categories`

- **HTTP:** `GET /politico/categories`
- **What:** Get Politico section navigation. Returns Politico's full public section navigation tree, grouped the same way the site's own nav menu groups it. Use a section's slug directly as the topic parameter on politico-topic.
- **Params:** _none_

### `politico_headlines`

- **HTTP:** `GET /politico/headlines`
- **What:** Get Politico site-wide headlines. Returns fresh headlines from Politico's public, site-wide RSS feed.
- **Params:** _none_

### `politico_topic`

- **HTTP:** `GET /politico/topic`
- **What:** Get Politico section archive. Returns the newest public Politico stories on one section archive page. topic is a section slug -- see politico-categories for the full known value space.
- **Params:** `topic` (string, **required**) — Politico section slug

## Reuters (6)

### `reuters_article`

- **HTTP:** `GET /reuters/article`
- **What:** Get a Reuters article's content. Returns one normal Reuters article's public metadata and body paragraphs from a canonical article URL. Live blogs, video and podcast pages, and subscriber-only or bot-challenged responses are not supported.
- **Params:** `url` (string, **required**) — Canonical Reuters article URL

### `reuters_articles`

- **HTTP:** `GET /reuters/articles`
- **What:** Get recent Reuters articles. Returns a page of recent Reuters articles: title, canonical URL, update time, and the lead image URL when available. The index covers the most recent 10,000 articles.
- **Params:** `page` (integer, optional) — Results page, 100 items per page

### `reuters_author`

- **HTTP:** `GET /reuters/author`
- **What:** Get a Reuters author profile. Returns a Reuters author's byline metadata, contact/social links, and recent articles from a canonical author URL.
- **Params:** `url` (string, **required**) — Canonical Reuters author URL

### `reuters_news`

- **HTTP:** `GET /reuters/news`
- **What:** Get fresh Reuters headlines. Returns fresh Reuters headlines with title, canonical URL, publication and update times, and the lead image when Reuters publishes one. Covers the most recent stories from Reuters' public news feed.
- **Params:** `page` (integer, optional) — Results page, 50 items per page

### `reuters_section`

- **HTTP:** `GET /reuters/section`
- **What:** Get recent articles in a Reuters section. Returns a page of one top-level Reuters section's recent articles: canonical URL, update time, lead image URL, and image caption. This feed does not publish titles; use /reuters/articles for a title-bearing index.
- **Params:** `page` (integer, optional) — Results page, 100 items per page; `section` (string, **required**) — Top-level Reuters section

### `reuters_sections`

- **HTTP:** `GET /reuters/sections`
- **What:** List Reuters sections. Lists every top-level Reuters section accepted by /reuters/section, with its slug, display name, and landing-page URL.
- **Params:** _none_

## Washington Post (5)

### `wapo_article`

- **HTTP:** `GET /wapo/article`
- **What:** Get a Washington Post article's content. Returns one public Washington Post article's metadata and body paragraphs from a canonical article URL. Metered articles that the site truncates are not available.
- **Params:** `url` (string, **required**) — Canonical Washington Post article URL

### `wapo_author`

- **HTTP:** `GET /wapo/author`
- **What:** Get a Washington Post staff author profile. Returns one Washington Post staff author's public profile: byline metadata, bio, contact/social links, and one page of their recent articles.
- **Params:** `page` (integer, optional) — 1-based page number; overrides any page number in url; `slug` (string, optional) — Washington Post people slug, e.g. adam-taylor; `url` (string, optional) — Canonical washingtonpost.com/people/<slug>/ URL, optionally with a ?page= query; alternative to slug

### `wapo_headlines`

- **HTTP:** `GET /wapo/headlines`
- **What:** Get the latest stories in a Washington Post section. Returns the first page of a Washington Post section front: each story's title, canonical URL, description, section, publication time, and lead image. Section must be a path returned by /wapo/sections.
- **Params:** `section` (string, **required**) — Section path from /wapo/sections

### `wapo_news`

- **HTTP:** `GET /wapo/news`
- **What:** Get the latest Washington Post stories. Returns The Washington Post's current public news-sitemap feed with titles, canonical URLs, publication times, and last-modified times.
- **Params:** _none_

### `wapo_sections`

- **HTTP:** `GET /wapo/sections`
- **What:** List Washington Post sections. Lists every Washington Post section accepted by /wapo/headlines, with its path slug, display name, and landing-page URL.
- **Params:** _none_
