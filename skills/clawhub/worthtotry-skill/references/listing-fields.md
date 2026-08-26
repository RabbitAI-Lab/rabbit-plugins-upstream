# Listing fields

Limits are enforced by the validator. Copy that overruns is rejected with an error, not truncated.

## The draft

| Field           | Limit | Rules                                                                          |
| --------------- | ----: | ------------------------------------------------------------------------------ |
| `name`          |    40 | Required. The product's name, not a sentence.                                  |
| `tagline`       |    60 | Required. No trailing period — it is rejected.                                 |
| `description`   |   600 | Required, minimum 40 characters. At least a couple of sentences.               |
| `targetKeyword` |   100 | Optional. One keyword, no commas. Leave empty unless the person supplies it.   |
| `firstComment`  |   200 | Optional. **No links.** Browser form only — you cannot set it.                 |
| `categories`    |     3 | At least 1, at most 3, no repeats.                                             |
| `screenshots`   |     5 | At least 1 required before review. Captured in the browser; you cannot supply. |

Also on the draft, and not settable by you:

- **logo** — required before review. Extracted from the page when the `logo` check passes, otherwise
  uploaded in the browser.
- **launchDate** — must be in the future. The person's choice; null means it publishes as soon as a
  moderator approves.
- **twitterHandle** — 1 to 15 letters, numbers or underscores, no `@`. You may pass this.
- **demoVideoUrl** — YouTube or Loom only. Browser form.

## Writing the copy

`name` is the product name. Do not append a category or a slogan to fill the 40 characters.

`tagline` says what it does for whom, in one line, with no full stop at the end. Write it so it
reads under the name on a card, not as a headline.

`description` is 40 to 600 characters. Lead with what the product does, then who it is for. Do not
restate the tagline. Do not open with "In today's fast-paced world" or any variant. No feature
bullets padded to reach the ceiling — a tight 200 characters beats a padded 590.

`targetKeyword` decides how the listing page is optimised for search. Leave it blank unless the
person names one. A guess here is worse than an empty field, and the audit deliberately never
suggests one.

## Pricing

One of: `free`, `freemium`, `paid`, `subscription`, `one_time`, `contact`.

The audit defaults to `contact` when the page does not say. Do not upgrade that to `free` because a
free tier looks likely — pick what the page actually claims, or leave the default and ask.

## Categories

At least one, at most three. Pass slugs; display names also resolve. Pick the categories a buyer
would browse, not every one that could apply.

| Slug               | Name             | Slug             | Name           |
| ------------------ | ---------------- | ---------------- | -------------- |
| `ai`               | AI               | `marketing`      | Marketing      |
| `analytics`        | Analytics        | `monitoring`     | Monitoring     |
| `cms`              | CMS              | `music`          | Music          |
| `communication`    | Communication    | `no-code`        | No Code        |
| `content-creation` | Content Creation | `open-source`    | Open Source    |
| `data`             | Data             | `productivity`   | Productivity   |
| `design-tools`     | Design Tools     | `sales`          | Sales          |
| `developer-tools`  | Developer Tools  | `search`         | Search         |
| `devops`           | DevOps           | `security`       | Security       |
| `e-commerce`       | E-Commerce       | `seo`            | SEO            |
| `education`        | Education        | `social-media`   | Social Media   |
| `finance`          | Finance          | `sustainability` | Sustainability |
| `food-drink`       | Food & Drink     | `travel`         | Travel         |
| `gaming`           | Gaming           | `video`          | Video          |
| `health-fitness`   | Health & Fitness | `web3`           | Web3           |
| `hr-recruiting`    | HR & Recruiting  | `writing`        | Writing        |
| `image`            | Image            | `other`          | Other          |
| `jobs-careers`     | Jobs & Careers   |                  |                |
| `launch-platforms` | Launch Platforms |                  |                |
| `legal`            | Legal            |                  |                |
| `lifestyle`        | Lifestyle        |                  |                |

Call `list_categories` to see which of these actually hold published tools, with counts.

## The two link-free fields

The **first comment** (200 characters) and a founder's **launch story** (title 120, body 200 to
20,000 characters) reject any content that links out. The error names the text that triggered it.

Rejected: markdown links and images, `<a>`, `<iframe>` and `<script>` tags, `http://` and `https://`
URLs, other URL schemes, `www.` prefixes, and a bare host followed by a path such as
`acme.com/pricing`.

Allowed, because they are prose and not links: `Next.js`, `config.json`, `v2.1.0`, `1.5s`, `16:9`,
and a bare product name like Vercel with no path after it.

Write both in plain prose. The listing already carries the link to the product.

## Comments

A comment is up to 2000 characters and rejects links under the same rule. One level of threading:
pass `parentId` to reply to a top-level comment.
