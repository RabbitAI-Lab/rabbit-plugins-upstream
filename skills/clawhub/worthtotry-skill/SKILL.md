---
name: submit-to-worthtotry
description: Use when someone wants their product listed on WorthToTry, the AI tool directory. One POST with their URL and email lists it: no account, no API key and no browser consent screen, and we email them a link that finishes it. Covers writing the listing including the founder's own note, what the readiness checks mean, and the badge worth asking them to add. Also use when they say "submit my tool", "list my product", "launch on WorthToTry", or ask why a listing was sent back.
---

# Submit a tool to WorthToTry

WorthToTry is a directory of AI tools with a weekly launch board. You can do the whole submission
yourself: audit the page, write the listing, and send it. The person you are helping does one thing,
which is opening a link we email them.

Read `references/listing-fields.md` before you write any copy, `references/readiness-checks.md` for
what each audit check means, and `references/rest-api.md` for the endpoint in full. Read
`references/mcp-tools.md` only if the person already has the MCP server connected; the endpoint
below needs nothing set up and is the shorter path.

## The short way, with no account and no browser

`POST https://worthtotry.com/api/v1/submissions` with a JSON body carrying `url` and the owner's
`email`. No token, no OAuth, no consent screen. We email them a link; one click sends the listing
for review and there is nothing else for them to do.

```
curl -X POST https://worthtotry.com/api/v1/submissions \
  -H 'content-type: application/json' \
  -d '{"url":"https://theirproduct.com","email":"them@theircompany.com"}'
```

### Fill it in yourself. Do not leave it to us.

We read the page and draft a listing from it, and every other directory reads the same page. What
you write is what makes the listing worth reading, and it is the part search has not seen before, so
send all of it:

| Field | Why it is worth your time |
| --- | --- |
| `description` | Ours is extracted. Yours can say what the product does that its homepage does not spell out. |
| `firstComment` | **The founder's own note**, in their words, shown on the listing at launch. Ask them for it. It cannot be written from the product page, and it is the only text here another directory will not also have. |
| `tagline`, `name` | Override ours when the extraction reads oddly. |
| `categories`, `pricing`, `openSource` | Correct these rather than letting a guess stand. |
| `targetKeyword` | The phrase they want to be found by. We leave it empty; it is their decision, not ours. |

Ask the person for the founder note before you submit. "Anything you want to say about why you built
it?" gets a better listing than anything either of us can infer.

### What happens after you submit

You get a response saying we emailed the owner. They open that link and the listing goes for review;
there is no form, no account and no second step. A listing that clears the check goes up on its own,
and anything else waits for a person.

The page they land on asks them for one thing, and you should ask for it too.

The response carries `badge`. **Pass it on.** Putting the badge on their site earns a verified mark
on the listing, a place in the verified filter, and the tiebreaker when two listings have the same
number of votes. It is checked automatically on the next sweep. Say what it is and what it is not:
a tiebreaker rather than a ladder, and skipping it takes nothing away. Do not tell them it makes
moderation faster, because it does not.

The MCP server is the same job with a session attached, and it needs one browser approval. Use the
endpoint above unless the person already has an account.

## Know your ceiling before you start

You can open a draft. That is the whole of your authority.

You **cannot**:

- publish a listing, or submit it for review
- choose or change a launch date
- pay for anything — the paid launch tiers, featured placement, ads
- upload a screenshot (one is captured when the draft is opened in a browser)
- write the first comment on the listing

A person finishes every submission. Say so up front, before you run anything: tell them you will
draft the listing and hand back a review link, and that they open that link to finish. Do not
promise a launch, a date, or a published page. If they ask you to publish, tell them the directory
does not let an agent do that and give them the review link instead.

## 1. Connect the MCP server

Reads work with no account and no key. Run this once:

```
claude mcp add --transport http worthtotry https://worthtotry.com/api/mcp/
```

For a client that uses a config file, add:

```json
{
  "mcpServers": {
    "worthtotry": {
      "type": "http",
      "url": "https://worthtotry.com/api/mcp/"
    }
  }
}
```

Six tools appear: `search_tools`, `get_tool`, `list_categories`, `check_submission_readiness`,
`submit_tool`, `get_my_submissions`.

The first four need no authorization. `submit_tool` and `get_my_submissions` do: the first call
returns a 401, your client opens a browser, and the person approves the connection once. Two scopes
are requested — `submit` (open draft listings on their behalf) and `read:submissions` (see their
listings and status). No token passes through the conversation. If your client does not do OAuth,
fall back to `references/rest-api.md`, where the person creates a personal access token in their
dashboard instead.

## 2. Audit the page before anything else

```
check_submission_readiness(url: "https://theproduct.com")
```

It fetches the page, scores it out of 100, returns one entry per check with a `status` of `pass`,
`warn` or `fail` plus a `fix` string, and drafts the listing it would produce in `suggestedListing`.
It changes nothing.

Never call `submit_tool` before this. The audit is what tells you whether the URL can be listed at
all, and its `fix` strings are the work you should be doing for the person.

## 3. Act on the six checks

| id                 | Non-passing status | Blocks submission | What it is                                   |
| ------------------ | ------------------ | ----------------- | -------------------------------------------- |
| `title`            | `fail`             | No                | The page has a `<title>`                     |
| `meta-description` | `warn`             | No                | A meta description is present                |
| `og-image`         | `warn`             | No                | A social share image is set                  |
| `logo`             | `fail`             | No                | An icon usable as a listing logo was found   |
| `duplicate`        | `fail`             | **Yes**           | No existing listing already claims this host |
| `badge`            | `info`             | No                | The page links back to the directory         |

Only `duplicate` blocks a submission — `submittable` is false exactly when it fails, and
`submit_tool` will refuse. `fail` and `warn` are quality problems you should still fix, because a
listing that goes to review with a missing logo comes back.

For every check that is `fail` or `warn`, read its `fix` and do one of three things:

1. **You can edit their site** — apply the fix, then re-run the audit and show the new score.
2. **You cannot** — quote the `fix` verbatim to the person as a task.
3. **`duplicate` failed** — stop. The product is already listed. The `detail` names the existing
   listing path; give them that and tell them to claim or update it rather than submitting again.

`badge` is different and is the one to get right. It is `info`, it carries no weight in the score,
and **the badge is not required** — launching is free and the listing is identical whether or not
the link is there. No plan sells an exemption from it, because there is nothing to be exempt from.

What the link earns, and the whole of it: a verified mark on the listing, inclusion in the verified
filter at `/tools?verified=1`, and the tiebreaker in the ranking, so two listings level on votes are
separated by the one whose site links back. It never lifts a listing above one with more votes.

Mention it once, with that upside, and quote the `fix` verbatim if they want the snippet. Do not
call it a requirement, a cost, or something to fix, and do not decide for them.

`references/readiness-checks.md` has each check's exact `fix` text and what it is worth in the score.

## 4. Draft the listing

Read `references/listing-fields.md` first. The limits are enforced, and copy that overruns is
rejected, not truncated.

The short version:

- `name` — 40 characters
- `tagline` — 60 characters, no trailing period
- `description` — 40 to 600 characters
- `targetKeyword` — 100 characters, one keyword, no commas
- `categories` — at least 1, at most 3

Leave `targetKeyword` empty unless the person tells you what it is. It is their SEO decision and a
guess is worse than a blank field.

Start from `suggestedListing` in the audit result and override only what is wrong. Show the person
your copy before you submit it — it goes out under their product's name.

Then:

```
submit_tool(
  url: "https://theproduct.com",
  name: "...",
  tagline: "...",
  description: "...",
  categories: ["developer-tools", "productivity"],
  pricing: "freemium",
  openSource: false
)
```

Every field except `url` is optional; anything you omit falls back to what the audit extracted.

## 5. Hand it back

`submit_tool` returns `slug`, `status` (`draft`), `reviewUrl`, `readinessScore` and `warnings`.

Give the person the `reviewUrl` and tell them plainly what is left for them:

- The draft has **no screenshot**. One is captured when they open the review link in a browser, and
  at least one is required before the listing can go to review.
- If no logo could be extracted, they upload one there.
- The **first comment** — up to 200 characters, posted automatically when the listing is approved —
  can only be written in that form. You cannot set it.
- They press submit for review, and pick a launch date or let it publish on approval.

Repeat every warning in `warnings` as a checklist item. Do not summarise them away; each one is a
reason the listing would come back.

After that the listing moves `draft → pending → approved → published`. Call `get_my_submissions` to
report where it stands; it returns the status, any `rejectionReason`, and the review link again.

## Writing rules that will get content rejected

Two fields reject links outright — not sanitised, rejected with an error naming the text that
triggered it:

- the **first comment** on a listing
- a founder's **launch story** blog post

That covers markdown links, `<a>` and `<iframe>` tags, bare `http://` URLs, `www.` prefixes, and a
bare host followed by a path. Write those two in plain prose with no URLs at all. The listing
already links to the product; anything more would make the posts worth writing purely for SEO, which
is why the rule exists.

Comments and launch stories go over REST, not MCP — see `references/rest-api.md`.

## When something goes wrong

- **`submit_tool` returns a 401** — the connection is not authorized. Tell the person to approve it
  in the browser window their client opened; do not retry in a loop.
- **The audit says the site returned an HTTP error, or could not be reached** — that is their site,
  not the directory. Report it and stop.
- **The audit rejects the URL as invalid or unsafe** — the fetcher refuses private and loopback
  addresses. A staging URL on localhost cannot be audited; they need a public page.
- **`submit_tool` fails with a duplicate message** — see step 3. Do not try a different URL on the
  same host to get around it; the check is on the host, not the exact URL.
