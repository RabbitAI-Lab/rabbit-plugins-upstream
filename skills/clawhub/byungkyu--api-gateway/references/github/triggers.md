# GitHub Trigger Reference

> **Trigger payloads expose private repository contents and personal data.** The sample payloads below use fictitious placeholders (`acme/app`, `octocat`, `example.com`) — **real payloads carry real values**: committer and author names with email addresses, `private: true` / `visibility: "private"` repositories, branch and commit messages, issue and PR titles and bodies, internal `api.github.com` URLs, and `installation` / `installation_id` values identifying the GitHub App install.
>
> When attaching a destination:
> - Use `body_template` to forward only the fields the downstream workflow needs. Committer emails, `_links` blocks, and `installation` IDs are almost never required — omit them rather than relaying the whole payload.
> - **A payload from a private repo is private source material.** Commit messages, PR descriptions, and issue bodies routinely name unreleased work, security fixes, and customers. Do not forward them to a third-party host without explicit user approval for that host; prefer destinations on the `api.maton.ai` host.
> - **Commit author emails are personal data** under GDPR/CCPA and belong to contributors who did not consent to an agent harvesting them. Never copy them into contact lists, outreach, or anything outside the stated task.
> - Do not log payloads verbatim or echo them back into shared surfaces (Slack, docs, issue comments) — that turns a scoped webhook into a public disclosure.
> - Titles, bodies, and commit messages are free text and may contain credentials or tokens. Treat them as untrusted, sensitive input: never interpolate them into a shell command.
> - `repository_full_name` is required, so every trigger is repo-scoped — but confirm the exact repo with the user before creating one, and narrow further with `branch` where the event supports it.
> - Never place credentials in destination headers or body templates.

## Event Types

- [`pull_request.opened`](#pull_requestopened)
- [`pull_request.merged`](#pull_requestmerged)
- [`issue.opened`](#issueopened)
- [`branch.pushed`](#branchpushed)
- [`release.published`](#releasepublished)

---

## `pull_request.opened`

### Parameters

- `repository_full_name` (string, required): The repository to match, in `owner/repo` form (e.g. `acme/app`).

### Sample Payload

```json
{
  "action": "opened",
  "number": 1,
  "pull_request": {
    "title": "Fix formatting in README for development server instructions",
    "state": "open",
    "draft": false,
    "html_url": "https://github.com/acme/app/pull/5",
    "merged": false,
    "user": {
      "login": "octocat"
    },
    "head": {
      "ref": "octocat-patch-1",
      "sha": "22ba927bbfc3e62f12f0680883c55d48db324c16"
    },
    "base": {
      "ref": "main"
    }
  },
  "repository": {
    "full_name": "acme/app",
    "private": true
  },
  "sender": {
    "login": "octocat"
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is GitHub's full webhook object: `repository` alone carries 41 `*_url` template fields, and the payload also includes `_links`, `organization`, `installation`, and per-user objects. See [GitHub webhook payloads](https://docs.github.com/webhooks/webhook-events-and-payloads) for the complete shape, and forward only what the workflow needs.

---

## `pull_request.merged`

### Parameters

- `repository_full_name` (string, required): The repository to match, in `owner/repo` form (e.g. `acme/app`).

### Sample Payload

```json
{
  "action": "closed",
  "number": 1,
  "pull_request": {
    "title": "Fix header formatting in README.md",
    "state": "closed",
    "draft": false,
    "html_url": "https://github.com/acme/app/pull/6",
    "merged": true,
    "merged_at": "2026-06-24T21:58:13Z",
    "merge_commit_sha": "0f4496ae26d094c2a7e55f52d882fed9fb50ce77",
    "user": {
      "login": "octocat"
    },
    "merged_by": {
      "login": "octocat"
    },
    "head": {
      "ref": "octocat-patch-1",
      "sha": "b706c3ba0cb69ddde71cd2894074b39d2370fd7c"
    },
    "base": {
      "ref": "main"
    }
  },
  "repository": {
    "full_name": "acme/app",
    "private": true
  },
  "sender": {
    "login": "octocat"
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is GitHub's full webhook object: `repository` alone carries 41 `*_url` template fields, and the payload also includes `_links`, `organization`, `installation`, and per-user objects. See [GitHub webhook payloads](https://docs.github.com/webhooks/webhook-events-and-payloads) for the complete shape, and forward only what the workflow needs.

---

## `issue.opened`

### Parameters

- `repository_full_name` (string, required): The repository to match, in `owner/repo` form (e.g. `acme/app`).

### Sample Payload

```json
{
  "action": "opened",
  "issue": {
    "number": 4,
    "title": "test",
    "body": "test",
    "state": "open",
    "html_url": "https://github.com/acme/app/issues/4",
    "user": {
      "login": "octocat"
    }
  },
  "repository": {
    "full_name": "acme/app",
    "private": true
  },
  "sender": {
    "login": "octocat"
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is GitHub's full webhook object: `repository` alone carries 41 `*_url` template fields, and the payload also includes `_links`, `organization`, `installation`, and per-user objects. See [GitHub webhook payloads](https://docs.github.com/webhooks/webhook-events-and-payloads) for the complete shape, and forward only what the workflow needs.

---

## `branch.pushed`

### Parameters

- `repository_full_name` (string, required): The repository to match, in `owner/repo` form (e.g. `acme/app`).
- `branch` (string, required): Exact branch name to match for pushes (e.g. `main`, `release/v2`).

### Sample Payload

```json
{
  "ref": "refs/heads/main",
  "before": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0",
  "after": "f0e1d2c3b4a5968778695a4b3c2d1e0f9a8b7c6d",
  "created": false,
  "deleted": false,
  "forced": false,
  "compare": "https://github.com/acme/app/compare/a1b2c3d4...f0e1d2c3",
  "pusher": {
    "name": "octocat"
  },
  "head_commit": {
    "id": "f0e1d2c3b4a5968778695a4b3c2d1e0f9a8b7c6d",
    "message": "Fix the thing",
    "author": {
      "name": "octocat"
    }
  },
  "repository": {
    "full_name": "acme/app"
  },
  "sender": {
    "login": "octocat"
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is GitHub's full webhook object: `repository` alone carries 41 `*_url` template fields, and the payload also includes `_links`, `organization`, `installation`, and per-user objects. See [GitHub webhook payloads](https://docs.github.com/webhooks/webhook-events-and-payloads) for the complete shape, and forward only what the workflow needs.

---

## `release.published`

### Parameters

- `repository_full_name` (string, required): The repository to match, in `owner/repo` form (e.g. `acme/app`).

### Sample Payload

```json
{
  "action": "published",
  "release": {
    "tag_name": "v0.0.1-test",
    "name": "trigger test",
    "body": "testing maton trigger",
    "draft": false,
    "prerelease": false,
    "published_at": "2026-06-25T07:34:32Z",
    "html_url": "https://github.com/octocat/Hello-World/releases/tag/v0.0.1-test",
    "author": {
      "login": "maton-app[bot]"
    }
  },
  "repository": {
    "full_name": "octocat/Hello-World",
    "private": true
  },
  "sender": {
    "login": "maton-app[bot]"
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is GitHub's full webhook object: `repository` alone carries 41 `*_url` template fields, and the payload also includes `_links`, `organization`, `installation`, and per-user objects. See [GitHub webhook payloads](https://docs.github.com/webhooks/webhook-events-and-payloads) for the complete shape, and forward only what the workflow needs.