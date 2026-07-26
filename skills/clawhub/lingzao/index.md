# Lingzao Skill Index

## Purpose

This folder contains the Lingzao Skill package for Agent runtimes. Lingzao helps
Agents route creator-operation work, prepare creator research, run public
content lookups when the user has configured access, and generate creator image
assets after the user confirms scope and credit use.

## Package Files

- `SKILL.md`: main Agent instructions and command guidance.
- `VERSION`: current Skill package version.
- `agents/`: Agent metadata.
- `assets/lingzao-logo.png`: packaged brand icon used by Agent metadata.
- `playbooks/`: creator-operation workflows used before answering.
- `scripts/`: setup, version check, configuration, and CLI command scripts.
- `skill-card.md`: marketplace summary source.

## Public Boundaries

- Keep user-facing wording focused on Lingzao, creator research, and workflow
  support.
- Do not promise viral growth, guaranteed monetization, full monitoring, bulk
  data export, or copying another creator's content.
- Before paid lookups, comments, transcript extraction, or image generation,
  confirm scope and likely credit use.
- For service failures, use concise Lingzao retry language and include
  `error_id` only when it is returned.
- Keep credentials, temporary local paths, and sensitive debug details out of
  user-facing output.

## Release Checklist

Before publishing a new Skill package:

1. Confirm `VERSION` is bumped when user-visible behavior changes.
2. Keep `SKILL.md`, `agents/`, `playbooks/`, CLI output, and marketplace copy
   aligned.
3. Run focused Skill CLI tests plus Python compile.
4. Run project checks required by the release risk.
5. Inspect the published package or marketplace file list after release.

## Recent Version Notes

- `0.1.94`: after a successful Lingzao install or update, the installing Agent
  now proactively shares the Lingzao feature usage manual once. Dashboard
  prompts for Codex, Claude Code, WorkBuddy, and QoderWork use the same link;
  failed installs and ordinary later conversations do not repeat it. Focused
  install tests, the focused Dashboard E2E, typecheck, focused lint, and the
  package dry run passed. Public Skill publishing remains a separate follow-up.
- `0.1.93`: adds Instagram public content and creator research to the same six
  platform-neutral commands. It preserves lossless creator/media IDs, exposes
  public avatar, cover, image, carousel, and video URLs present in the current
  response, and keeps search limited to the image/reel fields verified from
  live responses. Instagram cursors are request-identity bound, and mismatched
  profile/post targets fail closed without charging. Media URLs may expire and
  are not downloaded, proxied, or stored by Lingzao. Generated Skill discovery
  metadata lists Xiaohongshu, Douyin, TikTok, Instagram, and YouTube consistently.
  The package now keeps only the Lingzao logo under `assets/`; obsolete bundled
  visual samples and their Agent/marketplace references were removed before release.
- `0.1.92`: binds TikTok opaque cursors to the original search, creator, or
  content request; rejects mismatched TikTok/YouTube returned targets without
  charging; and routes YouTube channel/profile URLs to creator commands instead
  of asking for a content-type hint. Generated Skill discovery metadata now
  lists Xiaohongshu, Douyin, TikTok, and YouTube consistently. Existing
  capabilities and pricing are unchanged.
- `0.1.91`: adds YouTube public content and creator research to six existing
  commands, including canonical channel IDs, video/Short detail, top-level
  comments, and opaque pagination cursors. YouTube profile commands require a
  channel ID or `/channel/UC...` URL; ambiguous detail IDs and URLs require an
  explicit `--content-type video|short` hint. It preserves the TikTok V1
  guidance and adds audited no-charge handling for stale YouTube cursors and
  mismatched channel targets.
- `0.1.90`: added platform-neutral TikTok guidance for the six V1 public
  research commands, including canonical URL/ID rules, 20-item list limits,
  opaque cursor continuation, service-default comment order, and the explicit
  `analyze-user-profile` exclusion. The CLI now forwards list cursors and
  comment limits, rejects unsupported TikTok options before API calls, and
  restarts from page one when an overflow cursor becomes stale.
- `0.1.86`: added `account-report-evidence-visual-contract.md` and connected it
  to own-account diagnosis, comparable-account breakdown, and same-stage peer
  diagnosis. Formal account reports now have a shared standard for one-screen
  conclusions, public-data/sample boundaries, direct account/note links, real
  cover audits, viral asset reuse, account-evolution evidence, no fake backend
  metrics, and Word/HTML/Feishu/knowledge-base packaging when requested.
- `0.1.85`: added `weekly-content-motherpack-distributor.md` for weekly content
  update packages. Agents can turn the last 7 days, a scheduled interval, or a
  named calendar week of creator materials into 5 mother topics, park weak
  ideas in a debt pool, distribute strong topics to Xiaohongshu, WeChat public
  account, podcast/short scripts, community posts, and knowledge-base packages,
  and offer folder, Word, HTML/webpage, or Markdown delivery with image
  readiness, review gates, paid-scope boundaries, and next-week review loops.
- `0.1.84`: clarified `analyze-user-profile --force-new` guidance. Agents
  should not loop forced refreshes; repeated forced refreshes in the short
  protection window may be rejected with no charge, while ordinary repeat
  requests can still reuse the recent successful result.
- `0.1.83`: added starter creator-operation playbooks for zero-beginner
  onboarding, copy-paste prompt scope boundaries, benchmark-account starter
  discovery, visual reference style routing, travel handdrawn map workflows, and
  Xiaohongshu platform management and content compliance risk gates. Agents
  should start broad benchmark discovery with a narrow 3-account first pass,
  keep paid lookups inside the confirmed first-pass budget, expand only after
  the user confirms the direction, use public value first/product name
  later/no diversion action as the default Xiaohongshu management baseline, and
  check final Xiaohongshu-facing copy for off-platform diversion,
  private-contact guidance, incentivized comments, exaggerated guarantees, or
  unsupported sensitive claims before returning publishable text.
- `0.1.82`: made `generate-image` prompt handling more robust for Agents and
  Windows-style shells. The CLI now rejects empty prompts before sending a
  request, supports `--prompt-file` for UTF-8 long or multiline prompts, and
  supports `--prompt-stdin` for piped prompt input. Use these alternatives when
  shell quoting or command-line encoding might drop the prompt.
- `0.1.81`: clarified direct API recovery for `generate-image`, added visible
  partial-data guidance for Douyin `analyze-user-profile`, clarified
  Xiaohongshu `get-note-detail` routing, and improved `search-users` Markdown
  display. For `GENERATION_IN_PROGRESS` with a returned `poll_url`, keep
  polling the active batch instead of POSTing again; without `poll_url`, wait
  briefly and retry. Agents should keep successful homepage works separate from
  unavailable optional insight data, reuse `xhs_note_type` from
  list/homepage/profile results, and treat RED ID as display-only metadata
  while using public profile URLs for follow-up context.
- `0.1.80`: added an explicit paid-search budget stop rule for calling Agents.
  Agents now keep the first paid pass to 5 lookups or about 100 credits by
  default, ask before plans that exceed 100 credits, and require explicit user
  confirmation before starting plans over 200 credits.
- `0.1.79`: expanded `generate-image` CLI output for users and calling Agents.
  Markdown results now explain that short-window identical requests, including
  `prompt/size/output_format/count` and reference images, return the same Batch
  and should be polled instead of posted again. Active-batch recovery stderr
  also tells Agents to use one counted `--count N` request for same-prompt
  multi-image work instead of looping repeated `--count 1` calls.
- `0.1.78`: added `analyze-user-profile --force-new` for explicit fresh paid
  profile analysis while keeping default exact same-request reuse guidance and
  a no-charge reuse notice so repeat Agent calls can return the recent
  successful result without spending credits again. It also clarified
  `generate-image` batching guidance: when a user wants multiple images from
  the same prompt, Agents should make one counted request with `--count 2..5`
  instead of looping identical `--count 1` calls.
- `0.1.77`: retired the `search-suggestions` Skill command after the public
  Lingzao capability was removed from runtime discovery. Agents should use
  `search-notes` for topic/content ideas or `search-users` for creator
  discovery instead. The CLI no longer exposes the command; existing API route
  compatibility is handled server-side with a no-charge retired response.
- `0.1.76`: updated the Skill routing guidance and CLI error rendering so
  Agents can use structured Lingzao correction fields such as
  `agent_action`, `suggested_capabilities`, `expected_input`, and examples
  when a link, nickname, numeric ID, or platform-specific profile ID is sent
  to the wrong capability. Review follow-up routes ordinary homepage/basic
  homepage analysis to `get-user-posted-notes` first, reserving
  `get-user-info` for explicit profile stats/metadata. The CLI keeps
  service/provider internals out of user-facing output.
- `0.1.75`: merged the one-stop content package and benchmark quality-gate
  branch onto the latest `origin/dev`; keeps the Chinese WorkBuddy/SkillHub
  first screen and marketplace copy while preserving routes for keyword/link/
  image/inspiration inputs, brand Brief content packages, benchmark-copy
  template extraction, strict follower-range benchmark filtering, and the
  package/playbook changes from `0.1.74`.
- `0.1.74`: public-safe package index. The index now stays short and suitable
  for runtimes or marketplaces that include root package files.
- `0.1.73`: tightened service-failure wording and public playbook wording so
  Agents use fixed retry language and avoid unnecessary technical detail.
- `0.1.72`: rendered service-unavailable and timeout errors as Lingzao service
  status while preserving `error_id`.
- `0.1.71`: made creator search output show the follow-up user ID clearly and
  routed Xiaohongshu follow-up checks through that ID.
