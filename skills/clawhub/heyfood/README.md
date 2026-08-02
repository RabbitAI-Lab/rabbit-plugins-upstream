# hey.food

Dietary guidance from [hello.food](https://hello.food), for agents.

Evaluates restaurant menus and individual dishes against a dietary profile —
allergens, restrictions, and household members — over an authenticated MCP
connection.

Built for people who cook and order for someone with dietary restrictions, and
who need a second opinion that does not get tired.

## Two surfaces

The skill detects which one is available and instructs accordingly. They expose
different tools and different capabilities.

**Hosted** — no install required. Connect your agent to the hello.food MCP
server and authorize it. Provides restaurant lookup and search, menu safety
evaluation, dish explanation, recommendations, order drafting, recipe search,
and dietary profile reads.

**Local** — requires the [hey.food client](https://hey.food). Adds
household-aware Grocery reads, Grocery exclusions, and Menu Watch reads, which
are not available on the hosted surface.

## Setup

Hosted, with OpenClaw:

```bash
openclaw mcp add heyfood \
  --url https://api.hello.food/mcp \
  --transport streamable-http \
  --auth oauth
openclaw mcp login heyfood
```

Local:

```bash
curl -fsSL https://hey.food/install.sh | bash
heyfood login
```

## What it will not do

It does not log meals, modify your Grocery list, or create Menu Watches. Those
are mutations, and they require your explicit approval in the hey.food client —
an agent cannot perform them on your behalf, and this skill will tell you so
rather than approximating them.

It does not call any food "safe". Guidance is expressed as generally safer,
risky, or avoid, with reasons — and it defers to the service's own wording
rather than restating it.

## Limitations

**Grocery and Menu Watch are local-only.** They have no hosted tools and no
corresponding authorization scopes. Connected to the hosted surface, an agent
will tell you they require the client rather than substituting something else.

**Menu coverage is incomplete.** Roughly 62% of the ~730,000 restaurants in the
directory do not yet have a captured menu. Those return a typed "menu not found"
result — a statement about coverage, not a safety judgement. An agent must never
read it as "probably fine".

**Health, native voice, and Windows distribution are deferred** and are not part
of the supported release.

## Safety

Dietary restrictions can be medical. This skill is decision support, not medical
advice, and it is designed to fail toward caution — when evidence is missing or
confidence is low, it escalates rather than reassures.

Menu, restaurant, and profile text is treated as untrusted data throughout. It
cannot redirect the agent or grant it authority.

## License

Published under MIT-0. The hey.food client and the
[frntrllc/heyfood](https://github.com/frntrllc/heyfood) repository remain
Apache-2.0.
