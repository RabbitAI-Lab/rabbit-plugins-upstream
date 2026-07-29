---
name: agent4-io
description: Build and run grounded business agents on agent4.io over MCP — agents, knowledge bases, load-on-demand skills, stateful Storylines and page playbooks.
homepage: https://agent4.io/cookbook
user-invocable: true
metadata:
  {
    "openclaw":
      {
        "emoji": "🤖",
        "requires": { "env": ["AGENT4_API_KEY"] },
        "primaryEnv": "AGENT4_API_KEY"
      }
  }
---

# agent4.io skills — build agents over MCP

This skill drives the **agent4.io** platform through its remote MCP server: create grounded agents,
knowledge bases, load-on-demand skills, stateful Storylines and page playbooks — all from your agent.

## Connect the MCP server (once)

The tools live on a remote MCP endpoint. Add it to your agent, authenticating with your tenant API key
(set `AGENT4_API_KEY`; get a key from **console → Settings → Security**, shown once at creation):

- **URL:** `https://api.agent4.io/v1/mcp`
- **Header:** `X-API-Key: $AGENT4_API_KEY`
- **Transport:** streamable-http

For Claude Code / any MCP client that takes a shell command:

```bash
claude mcp add --transport http agent4-io https://api.agent4.io/v1/mcp --header "X-API-Key: $AGENT4_API_KEY"
```

Once connected, call `tenant_info()` to confirm you are on the right tenant, then follow the recipes
below. This skill is a mirror of the always-current Cookbook at https://agent4.io/cookbook.

## Use it as a slash command

This skill is invocable directly — `/agent4-io <what you want>` — and routes to the right recipe below:

- `/agent4-io create a support agent grounded in these docs` → build a grounded agent
- `/agent4-io build a knowledge base from this site + these PDFs` → create & populate a KB
- `/agent4-io author a load-on-demand skill for booking` → write a Skill
- `/agent4-io compile this intake flow into a Storyline` → design & publish a Storyline
- `/agent4-io set a page-aware opener for /pricing` → configure a page playbook
- `/agent4-io how much quota have I used?` → usage & quota
- `/agent4-io who are my heaviest users this week?` → look up users and their sessions
- `/agent4-io what is a Storyline?` → look up an agent4.io concept

(On Claude Code and Cursor, the installer also lays down finer-grained shortcuts —
`/agent4-agent`, `/agent4-kb`, `/agent4-skill`, `/agent4-storyline`, `/agent4-docs` — but they all just
hand off to this same skill; here a single `/agent4-io` covers them.)

---

# agent4.io — build agents over MCP

This guide is assembled from the agent4.io Cookbook (https://agent4.io/cookbook). Modules:

- **agent4-io-principles** (v2) — Read-first design principles: one job per agent, few skills, grounded, verified — how to configure agents that work.
- **agent4-io-recipes** (v2) — Connect to agent4.io over MCP, install the skills, and run end-to-end recipes.
- **agent4-io-admin** (v3) — Create and configure agents (soul/task/tools/skills), load-on-demand skills, page playbooks (how the chat opens per page); check usage/quota and look up end users and their sessions.
- **agent4-io-knowledge** (v3) — Build, populate, verify and query grounded knowledge bases.
- **agent4-io-storyline** (v2) — Compile multi-step processes into stateful, guided Storyline graphs.

---
name: agent4-io-principles
description: Read-first design principles: one job per agent, few skills, grounded, verified — how to configure agents that work.
version: 2
---

Read-first design principles: one job per agent, few skills, grounded, verified — how to configure agents that work.

## Design principles — read this first

Most "the agent gives bad answers" problems are configuration, not the model. Follow these before you
build, and the results hold up. Ignore them and it is easy to assemble something that looks plausible and
behaves badly — then mistake that for a platform limit.

## One agent, one job

Give each agent a **single, clearly bounded task**. A "does everything" agent — support *and* sales
*and* scheduling — has a diffuse `task`, competes with itself for attention, and answers each thing
worse. If you have three jobs, build three agents.

## Keep the skill count small

Attach **only the skills this agent's job needs — roughly five or fewer.** Skills are chosen by the model
from their one-line `description`; the more you attach, the harder that choice, and the more often it
loads the wrong one or none. A focused set with sharp "use this when…" descriptions beats a big pile.

- Each skill's `description` says **when** to reach for it, in one line.
- Procedures live in `instructions` (loaded on demand), never in `soul` (paid for every turn).
- If two skills overlap in *when*, merge them — overlapping triggers make the choice a coin-flip.

## Ground facts; put boundaries in the task

- Facts (rates, policy, catalogue) belong in a **knowledge base**, which is retrieved every turn — not
  in the prompt, where they go stale and un-cited. See [Build a knowledge base](/cookbook/build-a-knowledge-base).
- Constraints belong in **`task`**, as negatives: "never promise a date", "for a quote, call a tool".
  Negative boundaries stop drift better than positive description. Don't put safety rules in `soul` —
  the platform appends global moderation for you.
- Turn on `grounding_required` when answers must come from the material, not the model's priors.

## Prefer deterministic control where correctness matters

When an outcome must be reliable, don't leave it to the model. In Storylines, use `rule` / `user_choice`
exits for routing and reserve `ai` exits for genuine judgment. Model loops with an explicit counter and a
cap, not "the LLM will stop eventually". See [Modelling a process as a Storyline](/cookbook/modelling-a-process-as-a-storyline).

## Show the agent good patterns only

When you hand an agent examples, make them **correct** examples. Don't paste a "here's the wrong way"
snippet next to the right one — the model may imitate the nearest example rather than read the caveat.
Describe what to avoid in words; keep runnable examples exemplary.

## Verify — writing is not working

After every change, check it did what you intended. Creating an agent doesn't mean it's configured the
way you think; adding to a knowledge base doesn't mean the question retrieves.

```text
get_agent(name="Support")                                   # confirm the config that landed
search_knowledge_base(kb_name="Company policy", query="…")  # confirm the answer is retrievable
```

An empty `search` result means that question will be answered as "not covered" — find that now, not from
a customer.

## Hand back a deliverable, not "done"

After every action, don't just report that you finished — tell the user **what you produced, a clickable
link to view it in the console, and one line on how to use it.** They will ask "where do I see it?" and
"how do I use it?" anyway; answer both up front. URL-encode names that contain spaces.

| After you… | Hand back |
|---|---|
| Create or import into a **knowledge base** | Its page — which includes the **knowledge starmap** (a 3D view of what was ingested): `https://console.agent4.io/#/knowledge-bases/<name>` |
| Create an **agent** | Its page to review/test: `https://console.agent4.io/#/agents/<name>` — and note that to let end users reach it, they create a **share link** in the console |
| Create a **skill** | `https://console.agent4.io/#/skills/<name>` |
| Publish a **Storyline** | `https://console.agent4.io/#/storylines/<id>` (the id from `create_storyline`) |
| Register an **MCP server** | `https://console.agent4.io/#/mcp/<id>` |

For example, after importing documents into a knowledge base, reply with how many chunks landed, the link
above so they can open its **knowledge starmap** and see exactly what was ingested, and confirm whether
it's now attached to an agent (or how to attach it). A bare "done" just makes them ask.

---
name: agent4-io-recipes
description: Connect to agent4.io over MCP, install the skills, and run end-to-end recipes.
version: 2
---

Connect to agent4.io over MCP, install the skills, and run end-to-end recipes.

## Get started with the agent4.io agent skills

agent4.io ships a remote **MCP server** (the tools) plus a set of **skills** (how to use the tools).
Point your agent at the MCP endpoint, install the skills once, and every recipe below becomes an
executable, step-by-step procedure.

## Connect — one command

```bash
curl -fsSL https://api.agent4.io/v1/integration/install.sh | sh -s -- --key tk_YOUR_KEY
```

This adds the `agent4-io` MCP server and installs the skill modules for your agent. Get a key from
**console → Settings → Security** (the plaintext is shown once, at creation).

## Verify

```text
tenant_info()   # → confirms you are connected to the right tenant
```

## Keep it current

```bash
curl -fsSL https://api.agent4.io/v1/integration/install.sh | sh -s -- update
```

Re-pulls the skills and reports which modules changed. The MCP tools are remote, so they are always
current; only these skill docs are versioned.

## Slash commands

The installer also drops a few **slash commands** for agents that support them — Claude Code
(`~/.claude/commands/`) and Cursor (`.cursor/commands/`). They're shortcuts that hand your task to the
right skill:

- `/agent4-agent <what>` — create a grounded agent
- `/agent4-kb <name + source>` — build a knowledge base, import, verify, attach
- `/agent4-skill <when + what>` — author a load-on-demand skill
- `/agent4-storyline <process>` — compile a process into a Storyline and publish
- `/agent4-docs <question>` — look up an agent4.io concept or how-to

They carry no logic of their own — each just points at the matching `agent4-io-*` skill (which holds the
steps and best practices) and passes what you type. Codex users don't need them: its custom prompts are
deprecated in favour of skills, which are already installed.

## What to do next

- [Create a grounded support agent](/cookbook/create-support-agent)
- [Build and populate a knowledge base](/cookbook/build-a-knowledge-base)
- [Author a load-on-demand skill](/cookbook/create-a-skill)
- [Configure a page-aware chat opener](/cookbook/configure-page-playbooks)
- [Compile a flow into a Storyline](/cookbook/build-a-storyline)

Every recipe names the exact MCP tool and arguments — never "open this page and click".

---
name: agent4-io-admin
description: Create and configure agents (soul/task/tools/skills), load-on-demand skills, page playbooks (how the chat opens per page); check usage/quota and look up end users and their sessions.
version: 3
---

Create and configure agents (soul/task/tools/skills), load-on-demand skills, page playbooks (how the chat opens per page); check usage/quota and look up end users and their sessions.

## Create a grounded support agent

> **Principle — one agent, one job.** Give this agent a single, clearly bounded task. If the business
> has three jobs (support *and* sales *and* scheduling), build three agents — a "does everything" agent
> answers each thing worse. More in [Design principles](/cookbook/design-principles).

An agent is **soul + task + tools + skills + knowledge_bases**. `soul` is identity and voice; `task` is
the job and its boundaries — both go into the fixed prefix of the system prompt.

## 1. See what you can attach

```text
list_tools()             # tools available to this tenant (including connected MCP tools)
list_knowledge_bases()   # knowledge bases you can mount
```

## 2. Create it

```text
create_agent(
  name="Support",
  soul="You are the support assistant for Acme Loans. Professional and warm.",
  task="Answer questions about mortgage products and the application process. "
       "Never promise a disbursement date; never give legal or tax advice; "
       "for any specific quote, call a tool — do not answer from memory.",
  tools=["web_search"],
  knowledge_bases=["Company policy"],
  published=True,
)
```

## 3. Confirm what landed

```text
get_agent(name="Support")   # writing it doesn't mean it looks the way you intended
```

<Callout>
`published=True` means **visible**, not **usable**: an empty space = off. To let end users reach it,
create a share link or add the agent to a user's space (done in the console).
</Callout>

Boundaries belong in `task` — negative constraints ("never promise…") stop drift better than positive
description. Don't put safety rules in `soul`; the platform appends global moderation automatically. To
change one field later, use `update_agent(name, field=…)` — it merges, so it won't blank the rest.

> **Report back.** Give the user the agent's console link to review and test it —
> `https://console.agent4.io/#/agents/Support` — and note that to let end users reach it, they create a
> **share link** in the console (an empty space = off).

## Author a load-on-demand skill

> **Principle — keep the skill count small.** Attach only what this agent's job needs (≈5 or fewer).
> The model picks skills from their one-line `description`; the more you attach, the more often it loads
> the wrong one or none. If two skills overlap in *when*, merge them. More in
> [Design principles](/cookbook/design-principles).

A **skill** is a capability pack loaded on demand: the system prompt carries only its `description`
("when to use"); the model pulls the full `instructions` only when it judges the skill relevant. So the
`description` must be short and say *when*, or the model won't know to reach for it.

```text
list_skills()                                # what already exists

create_skill(
  name="refund-policy",
  description="Use when the user asks about refunds, cancellations or chargebacks.",
  instructions="The full procedure: eligibility windows, how to word the outcome, when to escalate …",
)

update_agent(name="Support", skills=["refund-policy"])   # attach it
```

Keep procedures in `instructions` (fetched on load), not in the agent's `soul` (which is in the prompt
every turn). A one-line `description` that says *when* is what makes the skill discoverable — a vague one
means the model never pulls it.

## Configure a page playbook (page-aware chat opener)

> **Principle — the opener is the only sentence guaranteed to be read.** A generic "How can I help?"
> converts a page visit into nothing. A playbook lets the *same* agent open differently on each page,
> already knowing where the visitor is. More in [Page playbooks](/concepts/playbooks).

A **page playbook** is a small briefing attached to a URL pattern. It has three parts:

- **`context`** — private background for the agent, **not shown** to the visitor (who lands on this
  page, what they're deciding, what they usually worry about). Write background, not facts: prices,
  quotas and policy belong in a [knowledge base](/cookbook/build-a-knowledge-base), which outranks it.
- **`greeting`** — the opening line the visitor actually sees.
- **`questions`** — up to four suggested questions, so a visitor who hasn't formed one can just pick.

The right playbook is chosen from the URL: resolution order is **explicit key → `url_pattern` →
default**. A single default catches every unmatched page, so nothing ever falls back to a blank box.

## 1. See what's already there

```text
list_page_contexts()   # existing playbooks: match rules, greeting mode, position, which is default
```

## 2. Create or replace one

```text
upsert_page_context(
  key="pricing",
  label="Pricing page",
  url_pattern="*/pricing",           # glob, path-only; ignores query string and trailing slash
  context="Visitors here are comparing plans and worrying about overage. "
          "They are usually the person who will sign off on the cost. "
          "Do not quote custom pricing in chat.",
  greeting="You're looking at our plans — want me to work out where overage would start for your volume?",
  questions=["What's included in the free plan?", "How is overage billed?", "Can I change plans later?"],
  greeting_mode="generated",         # generate opener + questions in the visitor's language (recommended)
  is_default=False,
)
```

`greeting_mode="generated"` writes the opener and questions per visitor language on the fly — so a
Spanish visitor gets a Spanish greeting without you authoring five versions. Use `"static"` only when
you want your exact `greeting`/`questions` verbatim.

## 3. Verify the match — always

```text
resolve_page_context(url="https://acme.com/pricing?ref=x")   # → which playbook this URL hits, and how
```

Globs are easy to get subtly wrong (a missing `*`, one path level too many). A mismatch has **no error
message** — the visitor just silently gets the default playbook. So after writing any `url_pattern`,
resolve a real URL and confirm `matched_by` is `url_pattern`, not `default`.

## 4. Set a catch-all default

```text
upsert_page_context(
  key="default",
  label="Everywhere else",
  context="General visitor to the site; intent unknown. Ask what brought them in before assuming.",
  greeting_mode="generated",
  is_default=True,                    # at most one default per tenant; setting this unsets any other
)
```

<Callout>
`upsert_page_context` is a **full replace**, not a patch: fields you omit fall back to defaults rather
than keeping their old value. To change one field, `list_page_contexts()` first, merge, then upsert.
</Callout>

Once playbooks have been live for a while, `page_context_stats()` shows which ones get opened and which
suggested questions get clicked — so you tune copy from data, not guesses.

> **Report back.** Give the user the console link to review and edit these —
> `https://console.agent4.io/#/page-contexts` — and confirm each `url_pattern` resolves the way they
> expect (step 3). The chat widget needs no code change for a static site; single-page apps that have
> no distinct URL per view can name a playbook by its `key` instead.

## Deleting things — point the user to the console

Deletions are deliberately **not** exposed as tools — they are irreversible, and from a conversation you
usually can't tell whether an agent or knowledge base is still used by something else. So when the user
asks you to delete something, **don't attempt it** — tell them exactly where to do it in the console at
[console.agent4.io](https://console.agent4.io), and offer to help with the safe parts (finding the item,
listing what depends on it) first.

| To delete… | Where in the console |
|---|---|
| An agent | Agents → open the agent → top-right **⋯ / Delete** |
| A knowledge base (and all its documents) | Knowledge → open the base → **Delete** |
| One document in a knowledge base | Knowledge → the base → **Documents** tab → the row → **Delete** |
| A skill | Skills → the skill → **Delete** (agents referencing it stop loading its guidance) |
| A user, space, or session | Users → the row → **Delete** |
| Revoke / re-issue an API key | Settings → **Security** → **Revoke** (then create a new one) |
| Change privacy mode / BYOK | Settings (this shifts compliance responsibility — confirm before changing) |

Before you send them off, it helps to **surface what would be affected**: e.g. list the agents that
mount a knowledge base (`list_agents` + `get_agent`) so they can see whether deleting it breaks anything.
That check is exactly why deletion is a human action in the console, not a tool call.

## Connect your own MCP server

Bring your own tools: register a **remote** MCP server and its tools become available to attach to your
agents. There is no "create MCP server" tool on purpose — registering a server means trusting it to run
against your tenant, so it is a deliberate action in the console (or a REST call), not something an agent
does on its own.

## 1. Register the server

In the console: **Tools / MCP → Add MCP server** — give it a name, choose the transport
(**Streamable HTTP** or **SSE**), and the URL plus any auth headers.

Or by REST, with your tenant key (`$BASE` = `https://api.agent4.io/v1`):

```bash
curl -X POST $BASE/mcp-servers -H "X-API-Key: $KEY" -H 'Content-Type: application/json' \
  -d '{"name":"my-tools","transport":"streamable_http",
       "config":{"url":"https://tools.example.com/mcp","headers":{"Authorization":"Bearer …"}}}'
```

Only **remote** transports are accepted. `stdio` (local commands) is rejected — the server runs on the
platform, not your machine, so a local command would be both useless to you and a code-execution risk.

## 2. See its tools

```text
list_mcp_servers()   # the MCP servers registered on your tenant
list_tools()         # every tool you can attach to an agent, including the ones from your servers
```

## 3. Attach the tools to an agent

```text
update_agent(name="Support", tools=["web_search", "…"])   # use tool names exactly as list_tools() reports them
```

The agent can now call those tools during a conversation. Keep the set focused — a handful of relevant
tools beats a big pile (see [Design principles](/cookbook/design-principles)).

## Built-in tools (and the system MCP)

You don't have to build the common tools — the platform ships them. Attach the ones this agent's job
needs with `update_agent(name, tools=[…])`; keep the set small (see [Design principles](/cookbook/design-principles)).
Always confirm the exact names on your tenant with `list_tools()` — that is the source of truth.

## The built-in tools

| Tool | What it does |
|---|---|
| `web_search` | Look something up on the open web. |
| `save_contact` | Capture the end user's contact details into their profile — the platform's lead-capture / records path. |
| `export_document` | Generate a structured document (a branded summary / report) for the conversation. |
| `schedule_followup` | Proactively follow up later ("check back in 2 days") — the message is sent for you. |
| `schedule_reminder` | Set a reminder for the end user; `list_reminders` / `cancel_reminder` manage them. |

`load_skill` is also built in, but you don't attach it — the model pulls a skill on its own when a
skill's `description` matches.

```text
list_tools()                                              # exact names available on your tenant
update_agent(name="Support", tools=["web_search", "save_contact", "schedule_followup"])
```

Capturing a contact with `save_contact` populates the user's record; combined with `ask_forms` on the
agent, structured intake lands as records you can review in the console.

## The system MCP — already installed

Every tenant gets a built-in **`system`** MCP server, enabled by default, with keyless tools for
**local time, weather, and IP geolocation** (city / region / timezone). You don't register it — it's
there. Its tools show up in `list_tools()` alongside the built-ins above, ready to attach.

So "what's the weather where the user is?" or "what's their local time?" work out of the box — the
platform injects the end user's client IP, so location-aware answers need no setup.

## Check usage and quota

Two read-only tools answer every "how much am I using?" question. Both return **metadata only** — token
counts and event counts — and **never any conversation content**.

## Where you stand against the quota

```text
tenant_info()                 # plan + monthly_token_quota (the ceiling)
usage_stats(group="total")    # tokens + events used so far this period
```

**Use case — "am I about to run out?"** Compare the total against `monthly_token_quota` from
`tenant_info`. Overage is billed in arrears, so surfacing "you're at 82% of this month's quota" lets the
user decide before it costs them.

## What's driving the cost

`usage_stats(group=…)` slices the same totals. Pick the group by the question you're answering:

```text
usage_stats(group="agent")    # which agent is busiest / burning the most tokens
usage_stats(group="user")     # which end user is heaviest — spot one runaway account
usage_stats(group="space")    # usage per customer space (multi-tenant fan-out)
usage_stats(group="day")      # trend over time — catch a spike the day it happens
usage_stats(group="model")    # cost mix across models — is an expensive model doing routine work?
```

**Use cases at a glance:**

- *"My bill jumped this month — why?"* → `group="day"` to find the spike, then `group="agent"` to see
  which agent it came from.
- *"Is one model doing work a cheaper one could?"* → `group="model"`, then consider
  `update_agent(name, model=…)` on the offenders.
- *"Which customer should I upsell / rate-limit?"* → `group="space"` or `group="user"`.

<Callout>
This is **metadata, not analytics on content**. It answers *how much* and *by whom/what*, never *what
was said*. Chat transcripts and end-user profiles are deliberately not reachable over MCP.
</Callout>

> **Report back.** Lead with the one number that matters — "You've used 4.2M of your 5M monthly tokens
> (84%)" — then the breakdown that explains it, and link the console for the full picture:
> `https://console.agent4.io/#/usage`.

## Look up users and their sessions

> **Principle — hand back a link, not a transcript.** These tools return *who* your users are and
> *how much* they chat — never the conversation text. Each result carries a `console_url`; give that to
> the user so they open and read the transcript in the console, where it renders properly.

Three read-only tools cover "who is using my agents, and how much":

## 1. The user directory

```text
list_end_users(sort="tokens24h")     # busiest first; sort="recent" for newest
list_end_users(q="alex")             # filter by name or external id
```

Each user comes back with sign-in method, email (if any), space/session/document counts, 24h token
usage, and a `console_url`. **Use case — "who's my heaviest user this week?"** → `sort="tokens24h"`,
then hand back the top user's `console_url`.

## 2. One user's detail

```text
get_end_user(uid="…")                # profile: name, contact email/phone, city, timezone, spaces
```

Profile fields only — no conversation content. Includes a `console_url` to their detail page.

## 3. Their sessions — metadata, then a link

```text
list_user_sessions(uid="…")          # per session: agent, AI-summarised title, message_count, tokens, time
```

**The messages themselves are not returned** — by design. You get the session's *shape* (which agent,
how long, when, an AI title) plus two links: `console_url` opens **that exact conversation** (the
console jumps straight to it and pops the transcript — no hunting through a long list), and
`user_console_url` opens the user's detail page. **Use case — "has this customer talked to us before,
and what about?"** → list their sessions, summarise the titles, and hand back the `console_url` of the
relevant one so they land right on that thread.

<Callout>
Why no transcript over MCP: chat content is your end users' data, and a tenant API key is held by
whatever agent you connected. So the platform returns **metadata + a console link**, and the raw
conversation is read by a human in the console — not streamed to an integrating agent.
</Callout>

> **Report back.** Lead with the answer ("Alex has 3 sessions, all about refinancing, most recent
> yesterday"), then paste the `console_url` of the relevant session so the user clicks straight into
> that exact thread — or `user_console_url` for the whole person.

---
name: agent4-io-knowledge
description: Build, populate, verify and query grounded knowledge bases.
version: 3
---

Build, populate, verify and query grounded knowledge bases.

## Build and populate a knowledge base

> **Principle — ground, then verify.** A knowledge base is a MUST-follow source, not a hint. Scope its
> coverage in `instructions`, and always confirm a real question retrieves *before* you rely on it — an
> empty search means the agent will answer "not covered". More in [Design principles](/cookbook/design-principles).

A mounted knowledge base is **auto-retrieved every turn** — the model does not decide whether to look;
relevance is by vector distance. That is deliberate: a KB is a MUST-follow source, not an optional tool.

## 1. Create it

```text
create_knowledge_base(
  name="Company policy",
  description="Mortgage policy and rates, effective 2026",     # for humans
  instructions="Authoritative current mortgage policy; overrides any industry norm. "
               "Covers home mortgages only; for car or personal loans, say so and hand off.",  # for the model
)
```

## 2. Add content

```text
add_knowledge_text(kb_name="Company policy", title="2026 late-fee rule",
                   content="From 1 July 2026 the daily late fee is 0.019% …")
```

Binary files (pdf/docx) and whole folders (zipped) go through `add_knowledge_file` — subfolders are
walked and each md/txt/pdf/html/docx is imported under its in-archive path.

## 3. ★ Verify retrieval — don't skip ★

```text
search_knowledge_base(kb_name="Company policy", query="how is the late fee calculated")
#   hits  → the agent can answer this
#   empty → the agent will treat it as "not covered" and say so
```

## 4. Mount it

```text
update_agent(name="Support", knowledge_bases=["Company policy"])
```

Don't write "always cite the passage" in `instructions` — that behaviour is built in. Only write what is
specific to *this* library: authority ordering, coverage boundaries, special usage (e.g. "quoting a rate
must state its effective date").

> **Report back — don't stop at "imported".** Tell the user how many chunks landed and give them the
> clickable link to open the knowledge base and its **knowledge starmap** (a 3D view of what was
> ingested): `https://console.agent4.io/#/knowledge-bases/Company%20policy` — then confirm it's attached
> to the agent.

## Let your agent query your knowledge base

Your connected agent can search **your own** knowledge bases directly — to ground an answer or pull a
fact mid-task.

```text
list_knowledge_bases()                                  # what's available
search_knowledge_base(kb_name="Company policy", query="late fee for 60 days overdue")
```

Access is authenticated by your tenant API key, so **private knowledge stays private** — there is no
unauthenticated path to it. If the tenant is in **BYOK / privacy mode**, content endpoints return `403`
(metadata such as usage still works), by design.

Use retrieval to *ground*, not to decide: quote what comes back; if nothing does, say it isn't covered
rather than guessing.

---
name: agent4-io-storyline
description: Compile multi-step processes into stateful, guided Storyline graphs.
version: 2
---

Compile multi-step processes into stateful, guided Storyline graphs.

## Compile a flow into a Storyline

A **Storyline** is a directed graph hung on an agent: it turns "answer one question" into "carry a whole
task end to end" (intake, tutoring, coaching…). Nodes are steps (each with its own task / skills / kb /
tools + writable profile dimensions); exits carry conditions (`ai` / `user_choice` / `rule` / `callback`
/ `goto_storyline`). The runtime **never edits the agent's soul or safety boundary** — it is constant from
the first node to the last, which is exactly what a regulated or child-facing product needs.

## Create a draft

```text
create_storyline(
  agent_name="Support", key="loan-intake", name="Loan intake",
  profile_schema={"docs_ready": {"type": "bool"}},          # dims that accumulate across nodes
  graph={"nodes": [
    {"node_key": "n1", "title": "Understand need", "flags": {"is_entry": True},
     "on_enter_opening": "Hi — which kind of loan are you applying for?",
     "exits": [{"kind": "ai", "label": "need clear", "to_node_key": "n2",
                "ai_criteria": "the user stated the loan type and rough amount"}]},
    {"node_key": "n2", "title": "Collect documents",
     "task": "Collect the checklist items; chase missing ones across turns.",
     "exits": [{"kind": "user_choice", "label": "documents ready", "to_node_key": "n3",
                "user_choice": {"button_text": "I've uploaded everything"},
                "writes": [{"ref": "dim", "key": "docs_ready", "op": "set", "value": True}]}]},
    {"node_key": "n3", "title": "Hand off", "task": "Summarise the case and hand off to a human.",
     "flags": {"is_terminal": True}, "exits": []}
  ]},
  allow_agent_enroll=True,
  enroll_trigger="the visitor says they want to apply for a loan",
)
```

## ★ Validate, then publish ★

```text
validate_storyline(storyline_id="…")   # → {"ok": true} is required to publish
publish_storyline(storyline_id="…")    # freezes an immutable version and goes live
```

## Enrollment — who enters, and when (all require publishing)

- `is_default=True` — one per agent; auto-enrolls on the first conversation.
- `allow_agent_enroll=True` + `enroll_trigger` — the agent enrolls the user when it judges the trigger.
- Manual assignment in the console.

Exits are **priority-ordered** (list order): deterministic `rule` / `user_choice` / `callback` are judged
first, `ai` last. Build if/else, retry loops and AND-joins out of deterministic exits — don't gamble on
the LLM. Edit a draft with `update_storyline` (PUT semantics; keep every `node_key` stable, since exits
and the funnel reference it).

> **Report back.** Return the published Storyline's console link —
> `https://console.agent4.io/#/storylines/<id>` (the id from `create_storyline`) — with a one-line
> summary of the flow and how a user enters it.

## Modelling a process as a Storyline — the right way

Turning a complex process into a Storyline is a modelling exercise, not a transcription. The mechanics
are in [Compile a flow into a Storyline](/cookbook/build-a-storyline); this is *how to think about it* so
the result is reliable rather than a graph that mostly works.

## Start from the profile, then the decision points

Before drawing nodes, decide **what you are tracking** — that is the `profile_schema` (e.g. `docs_ready`,
`risk_flag`, `attempts`). Then map the **real decision points**, not just the happy path. Every place the
conversation can branch or fail is a node with exits; a flow that only models the ideal path breaks the
first time a user does something unexpected.

## One node = one coherent step

A node should do one thing a person would name ("collect documents", "confirm identity"). Don't cram a
whole sub-process into a single node's `task` and hope the model sequences it — you lose the ability to
branch, resume and measure. If a node's task has "and then, and then", it's several nodes.

## Make branching deterministic where the outcome must be reliable

- Route on **`rule`** (against profile dims) or **`user_choice`** when the branch must be predictable.
  Reserve **`ai`** exits for real judgment ("did they actually describe their problem?").
- Exits are **priority-ordered** — put the deterministic ones first, the `ai` fallback last.
- Model a retry loop with a back-edge plus a `writes` counter (`op: "inc"`) and a `rule` cap. Never rely
  on the model to decide it has looped enough.

## Keep identity and safety on the agent, not the node

The agent's `soul` and safety boundary are constant across the whole Storyline — that is the point. Don't
try to re-state the persona or re-impose safety per node; nodes only add task/skills/kb/tools and write
profile dims.

## Keep node_keys stable; validate before publish

`node_key`s are the identity exits and the funnel reference. When you edit with `update_storyline`, keep
them stable — renaming a node silently orphans its exits. Always `validate_storyline` before
`publish_storyline`; it catches unreachable nodes, dead ends and dangling exits.

## Don't over-model

If the task is a single question and answer, it is **not** a Storyline — it's an agent with a knowledge
base. Reach for a Storyline when there is genuine multi-step state to carry (intake, tutoring, a guided
application). Modelling a one-shot Q&A as a graph adds cost and failure modes for nothing.

## Common ways it goes wrong (avoid these)

- **Happy-path only** — no exit for "user is confused" or "didn't provide it", so the flow stalls.
- **Everything is an `ai` exit** — routing becomes a gamble; the same input takes different paths.
- **A mega-node** — one node's `task` describes the entire process; nothing can branch or resume.
- **Unbounded loops** — a back-edge with no counter and no cap.
- **Restating safety per node** — noise that competes with the agent's actual boundary.

Fix these by naming the real states and moving each decision onto a deterministic exit.

## Parallel steps — do several things, then continue

Some steps aren't a line — they're "do all of these, in any order, each with its own follow-ups, and
continue only when every one is done." A visa application is the classic case: passport, bank statement
and invitation letter each need collecting and a *different* review, but you can't submit until all three
pass. That's a **parallel** node (a fork / AND-join), a first-class node type — you don't hand-wire
completion flags.

## How it works

A `parallel` node declares several **required branches**, each pointing to the entry of its own sub-flow.
The engine presents the unfinished branches as choices, tracks completion natively (entering a branch
records it; returning to the parallel node marks it done), and takes the node's **join exit** — the first
exit with a `to_node_key` — **automatically, once every branch is complete.** You don't evaluate that
condition yourself; the label is just for humans. Each branch can be a full multi-node sub-flow with its
own checks and loops; its last step simply takes a normal exit back to the parallel node.

```text
create_storyline(
  agent_name="Visa", key="visa-docs", name="Visa documents",
  graph={"nodes": [
    {"node_key": "collect", "title": "Collect all documents", "type": "parallel",
     "flags": {"is_entry": True},
     "parallel": {"branches": [
       {"key": "passport", "label": "Passport",         "to_node_key": "p1"},
       {"key": "bank",     "label": "Bank statement",   "to_node_key": "b1"},
       {"key": "invite",   "label": "Invitation letter","to_node_key": "i1"}
     ]},
     "exits": [{"kind": "ai", "label": "all documents cleared", "to_node_key": "submit",
                "ai_criteria": "all required documents have been checked"}]},

    {"node_key": "p1", "title": "Check passport", "task": "Verify validity ≥ 6 months; if not, tell the user what to renew.",
     "exits": [{"kind": "ai", "label": "passport ok", "to_node_key": "collect", "ai_criteria": "passport is valid and legible"}]},
    {"node_key": "b1", "title": "Check bank statement", "task": "Confirm 3 months of history and a sufficient balance.",
     "exits": [{"kind": "ai", "label": "bank ok", "to_node_key": "collect", "ai_criteria": "statement covers 3 months and meets the threshold"}]},
    {"node_key": "i1", "title": "Check invitation", "task": "Confirm host details and dates match the trip.",
     "exits": [{"kind": "ai", "label": "invite ok", "to_node_key": "collect", "ai_criteria": "invitation is consistent with the trip"}]},

    {"node_key": "submit", "title": "Submit application", "task": "Package the cleared documents and submit.",
     "flags": {"is_terminal": True}, "exits": []}
  ]}
)
```

The applicant can supply the three documents in any order; each returns to `collect` when it clears.
`submit` is **unreachable until all three branches are done** — the engine only takes the join exit then.

Give each branch as much of its own flow as it needs — a passport that's expiring can loop through a
"renew and re-upload" node before it returns; the bank branch can ask for a top-up statement. Keep the
branch `key`s unique. Then `validate_storyline` before publishing — it flags a parallel node with no
branches, a branch pointing at a missing node, or no join exit.
