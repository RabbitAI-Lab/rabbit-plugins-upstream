# GitHub access policy

An access policy limits which endpoints GitHub connections may call through Maton. GitHub doesn't offer a choice of OAuth scopes, so an access policy is the way to narrow a connection. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/github#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for GitHub: its 338 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create github --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "advisories"},
    {"method": "GET", "path": "advisories/{id}"},
    {"method": "GET", "path": "agents/**"},
    {"method": "GET", "path": "apps/{id}"},
    {"method": "GET", "path": "codes_of_conduct"},
    {"method": "GET", "path": "codes_of_conduct/{id}"},
    {"method": "GET", "path": "emojis"},
    {"method": "GET", "path": "events"},
    {"method": "GET", "path": "gists"},
    {"method": "GET", "path": "gists/public"},
    {"method": "GET", "path": "gists/starred"},
    {"method": "GET", "path": "gists/{id}"},
    {"method": "GET", "path": "gists/{id}/comments"},
    {"method": "GET", "path": "gists/{id}/comments/{id}"},
    {"method": "GET", "path": "gists/{id}/commits"},
    {"method": "GET", "path": "gists/{id}/forks"},
    {"method": "GET", "path": "gists/{id}/star"},
    {"method": "GET", "path": "gists/{id}/{id}"},
    {"method": "GET", "path": "gitignore/templates"},
    {"method": "GET", "path": "gitignore/templates/{id}"},
    {"method": "GET", "path": "installation/repositories"},
    {"method": "GET", "path": "issues"},
    {"method": "GET", "path": "licenses"},
    {"method": "GET", "path": "licenses/{id}"},
    {"method": "POST", "path": "markdown"},
    {"method": "POST", "path": "markdown/raw"},
    {"method": "GET", "path": "meta"},
    {"method": "GET", "path": "networks/{id}/{id}/events"},
    {"method": "GET", "path": "notifications"},
    {"method": "GET", "path": "notifications/threads/{id}"},
    {"method": "GET", "path": "notifications/threads/{id}/subscription"},
    {"method": "GET", "path": "octocat"},
    {"method": "GET", "path": "organizations/**"},
    {"method": "GET", "path": "orgs/{id}"},
    {"method": "GET", "path": "orgs/{id}/actions/**"},
    {"method": "GET", "path": "orgs/{id}/agents/**"},
    {"method": "GET", "path": "orgs/{id}/artifacts/**"},
    {"method": "POST", "path": "orgs/{id}/attestations/bulk-list"},
    {"method": "GET", "path": "orgs/{id}/attestations/repositories"},
    {"method": "GET", "path": "orgs/{id}/attestations/{id}"},
    {"method": "GET", "path": "orgs/{id}/blocks"},
    {"method": "GET", "path": "orgs/{id}/blocks/{id}"},
    {"method": "GET", "path": "orgs/{id}/campaigns"},
    {"method": "GET", "path": "orgs/{id}/campaigns/{id}"},
    {"method": "GET", "path": "orgs/{id}/code-scanning/**"},
    {"method": "GET", "path": "orgs/{id}/code-security/**"},
    {"method": "GET", "path": "orgs/{id}/codespaces/**"},
    {"method": "GET", "path": "orgs/{id}/copilot-spaces/**"},
    {"method": "GET", "path": "orgs/{id}/copilot/**"},
    {"method": "GET", "path": "orgs/{id}/dependabot/**"},
    {"method": "GET", "path": "orgs/{id}/docker/conflicts"},
    {"method": "GET", "path": "orgs/{id}/events"},
    {"method": "GET", "path": "orgs/{id}/failed_invitations"},
    {"method": "GET", "path": "orgs/{id}/insights/**"},
    {"method": "GET", "path": "orgs/{id}/installation"},
    {"method": "GET", "path": "orgs/{id}/installations"},
    {"method": "GET", "path": "orgs/{id}/interaction-limits"},
    {"method": "GET", "path": "orgs/{id}/interaction-limits/pulls/creation-cap"},
    {"method": "GET", "path": "orgs/{id}/invitations"},
    {"method": "GET", "path": "orgs/{id}/invitations/{id}/teams"},
    {"method": "GET", "path": "orgs/{id}/issue-fields"},
    {"method": "GET", "path": "orgs/{id}/issue-types"},
    {"method": "GET", "path": "orgs/{id}/issues"},
    {"method": "GET", "path": "orgs/{id}/members"},
    {"method": "GET", "path": "orgs/{id}/members/{id}"},
    {"method": "GET", "path": "orgs/{id}/members/{id}/codespaces"},
    {"method": "GET", "path": "orgs/{id}/members/{id}/copilot"},
    {"method": "GET", "path": "orgs/{id}/memberships/{id}"},
    {"method": "GET", "path": "orgs/{id}/migrations/**"},
    {"method": "GET", "path": "orgs/{id}/organization-roles/**"},
    {"method": "GET", "path": "orgs/{id}/outside_collaborators"},
    {"method": "GET", "path": "orgs/{id}/packages/**"},
    {"method": "GET", "path": "orgs/{id}/personal-access-token-requests"},
    {"method": "GET", "path": "orgs/{id}/personal-access-token-requests/{id}/repositories"},
    {"method": "GET", "path": "orgs/{id}/personal-access-tokens"},
    {"method": "GET", "path": "orgs/{id}/personal-access-tokens/{id}/repositories"},
    {"method": "GET", "path": "orgs/{id}/private-registries/**"},
    {"method": "GET", "path": "orgs/{id}/projectsV2/**"},
    {"method": "GET", "path": "orgs/{id}/properties/**"},
    {"method": "GET", "path": "orgs/{id}/public_members"},
    {"method": "GET", "path": "orgs/{id}/public_members/{id}"},
    {"method": "GET", "path": "orgs/{id}/repos"},
    {"method": "GET", "path": "orgs/{id}/rulesets/**"},
    {"method": "GET", "path": "orgs/{id}/secret-scanning/custom-patterns"},
    {"method": "GET", "path": "orgs/{id}/secret-scanning/pattern-configurations"},
    {"method": "GET", "path": "orgs/{id}/security-advisories"},
    {"method": "GET", "path": "orgs/{id}/security-managers"},
    {"method": "GET", "path": "orgs/{id}/settings/**"},
    {"method": "GET", "path": "orgs/{id}/teams/**"},
    {"method": "GET", "path": "rate_limit"},
    {"method": "GET", "path": "repos/{id}/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/artifacts"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/artifacts/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/artifacts/{id}/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/cache/**"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/caches/**"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/concurrency_groups"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/concurrency_groups/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/jobs/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/jobs/{id}/logs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/jobs/{id}/steps/{id}/logs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/oidc/customization/sub"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/organization-secrets"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/organization-variables"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/permissions/**"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/policies"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/policies/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runners/**"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/approvals"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/artifacts"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/attempts/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/attempts/{id}/jobs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/attempts/{id}/logs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/concurrency_groups"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/jobs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/logs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/pending_deployments"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/runs/{id}/timing"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/secrets/**"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/variables/**"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/workflows"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/workflows/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/workflows/{id}/runs"},
    {"method": "GET", "path": "repos/{id}/{id}/actions/workflows/{id}/timing"},
    {"method": "GET", "path": "repos/{id}/{id}/activity"},
    {"method": "GET", "path": "repos/{id}/{id}/agents/**"},
    {"method": "GET", "path": "repos/{id}/{id}/assignees"},
    {"method": "GET", "path": "repos/{id}/{id}/assignees/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/attestations/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/autolinks"},
    {"method": "GET", "path": "repos/{id}/{id}/autolinks/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/automated-security-fixes"},
    {"method": "GET", "path": "repos/{id}/{id}/branches/**"},
    {"method": "GET", "path": "repos/{id}/{id}/check-runs/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/check-runs/{id}/annotations"},
    {"method": "GET", "path": "repos/{id}/{id}/check-suites/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/check-suites/{id}/check-runs"},
    {"method": "GET", "path": "repos/{id}/{id}/code-quality/**"},
    {"method": "GET", "path": "repos/{id}/{id}/code-scanning/**"},
    {"method": "GET", "path": "repos/{id}/{id}/code-security-configuration"},
    {"method": "GET", "path": "repos/{id}/{id}/codeowners/errors"},
    {"method": "GET", "path": "repos/{id}/{id}/codespaces/**"},
    {"method": "GET", "path": "repos/{id}/{id}/collaborators"},
    {"method": "GET", "path": "repos/{id}/{id}/collaborators/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/collaborators/{id}/permission"},
    {"method": "GET", "path": "repos/{id}/{id}/comments"},
    {"method": "GET", "path": "repos/{id}/{id}/comments/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/comments/{id}/reactions"},
    {"method": "GET", "path": "repos/{id}/{id}/commits/**"},
    {"method": "GET", "path": "repos/{id}/{id}/community/profile"},
    {"method": "GET", "path": "repos/{id}/{id}/compare/**"},
    {"method": "GET", "path": "repos/{id}/{id}/contents/**"},
    {"method": "GET", "path": "repos/{id}/{id}/contributors"},
    {"method": "GET", "path": "repos/{id}/{id}/copilot/cloud-agent/configuration"},
    {"method": "GET", "path": "repos/{id}/{id}/copilot/code-review/settings"},
    {"method": "GET", "path": "repos/{id}/{id}/dependabot/**"},
    {"method": "GET", "path": "repos/{id}/{id}/dependency-graph/**"},
    {"method": "GET", "path": "repos/{id}/{id}/deployments"},
    {"method": "GET", "path": "repos/{id}/{id}/deployments/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/deployments/{id}/statuses"},
    {"method": "GET", "path": "repos/{id}/{id}/deployments/{id}/statuses/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/environments/**"},
    {"method": "GET", "path": "repos/{id}/{id}/events"},
    {"method": "GET", "path": "repos/{id}/{id}/forks"},
    {"method": "GET", "path": "repos/{id}/{id}/git/blobs/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/git/commits/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/git/matching-refs/**"},
    {"method": "GET", "path": "repos/{id}/{id}/git/ref/**"},
    {"method": "GET", "path": "repos/{id}/{id}/git/tags/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/git/trees/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/hash-algorithm"},
    {"method": "GET", "path": "repos/{id}/{id}/immutable-releases"},
    {"method": "GET", "path": "repos/{id}/{id}/installation"},
    {"method": "GET", "path": "repos/{id}/{id}/interaction-limits/**"},
    {"method": "GET", "path": "repos/{id}/{id}/invitations"},
    {"method": "GET", "path": "repos/{id}/{id}/issue-types"},
    {"method": "GET", "path": "repos/{id}/{id}/issues"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/comments"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/comments/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/comments/{id}/reactions"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/events"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/events/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/artifacts"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/artifacts/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/assignees/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/comments"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/dependencies/blocked_by"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/dependencies/blocking"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/events"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/issue-field-values"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/labels"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/parent"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/reactions"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/relates_to"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/sub_issues"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/suggestions"},
    {"method": "GET", "path": "repos/{id}/{id}/issues/{id}/timeline"},
    {"method": "GET", "path": "repos/{id}/{id}/keys"},
    {"method": "GET", "path": "repos/{id}/{id}/keys/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/labels"},
    {"method": "GET", "path": "repos/{id}/{id}/labels/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/languages"},
    {"method": "GET", "path": "repos/{id}/{id}/license"},
    {"method": "GET", "path": "repos/{id}/{id}/milestones"},
    {"method": "GET", "path": "repos/{id}/{id}/milestones/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/milestones/{id}/labels"},
    {"method": "GET", "path": "repos/{id}/{id}/notifications"},
    {"method": "GET", "path": "repos/{id}/{id}/pages"},
    {"method": "GET", "path": "repos/{id}/{id}/pages/builds"},
    {"method": "GET", "path": "repos/{id}/{id}/pages/builds/latest"},
    {"method": "GET", "path": "repos/{id}/{id}/pages/builds/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/pages/deployments/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/planning-statuses"},
    {"method": "GET", "path": "repos/{id}/{id}/private-vulnerability-reporting"},
    {"method": "GET", "path": "repos/{id}/{id}/properties/values"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/comments"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/comments/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/comments/{id}/reactions"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/comments"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/commits"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/files"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/merge"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/merge-async/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/requested_reviewers"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/reviews"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/reviews/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/pulls/{id}/reviews/{id}/comments"},
    {"method": "GET", "path": "repos/{id}/{id}/readme"},
    {"method": "GET", "path": "repos/{id}/{id}/readme/**"},
    {"method": "GET", "path": "repos/{id}/{id}/releases"},
    {"method": "GET", "path": "repos/{id}/{id}/releases/assets/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/releases/latest"},
    {"method": "GET", "path": "repos/{id}/{id}/releases/tags/**"},
    {"method": "GET", "path": "repos/{id}/{id}/releases/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/releases/{id}/assets"},
    {"method": "GET", "path": "repos/{id}/{id}/releases/{id}/reactions"},
    {"method": "GET", "path": "repos/{id}/{id}/rules/branches/**"},
    {"method": "GET", "path": "repos/{id}/{id}/rulesets/**"},
    {"method": "GET", "path": "repos/{id}/{id}/secret-scanning/custom-patterns"},
    {"method": "GET", "path": "repos/{id}/{id}/secret-scanning/scan-history"},
    {"method": "GET", "path": "repos/{id}/{id}/security-advisories/**"},
    {"method": "GET", "path": "repos/{id}/{id}/stacks"},
    {"method": "GET", "path": "repos/{id}/{id}/stacks/{id}"},
    {"method": "GET", "path": "repos/{id}/{id}/stargazers"},
    {"method": "GET", "path": "repos/{id}/{id}/stargazers/count"},
    {"method": "GET", "path": "repos/{id}/{id}/stargazers/history"},
    {"method": "GET", "path": "repos/{id}/{id}/stats/**"},
    {"method": "GET", "path": "repos/{id}/{id}/subscribers"},
    {"method": "GET", "path": "repos/{id}/{id}/subscription"},
    {"method": "GET", "path": "repos/{id}/{id}/tags"},
    {"method": "GET", "path": "repos/{id}/{id}/tarball/**"},
    {"method": "GET", "path": "repos/{id}/{id}/teams"},
    {"method": "GET", "path": "repos/{id}/{id}/topics"},
    {"method": "GET", "path": "repos/{id}/{id}/traffic/**"},
    {"method": "GET", "path": "repos/{id}/{id}/vulnerability-alerts"},
    {"method": "GET", "path": "repos/{id}/{id}/zipball/**"},
    {"method": "GET", "path": "repositories"},
    {"method": "GET", "path": "search/code"},
    {"method": "GET", "path": "search/commits"},
    {"method": "GET", "path": "search/issues"},
    {"method": "GET", "path": "search/labels"},
    {"method": "GET", "path": "search/repositories"},
    {"method": "GET", "path": "search/topics"},
    {"method": "GET", "path": "search/users"},
    {"method": "GET", "path": "teams/**"},
    {"method": "GET", "path": "user"},
    {"method": "GET", "path": "user/blocks"},
    {"method": "GET", "path": "user/blocks/{id}"},
    {"method": "GET", "path": "user/codespaces/**"},
    {"method": "GET", "path": "user/docker/conflicts"},
    {"method": "GET", "path": "user/emails"},
    {"method": "GET", "path": "user/followers"},
    {"method": "GET", "path": "user/following"},
    {"method": "GET", "path": "user/following/{id}"},
    {"method": "GET", "path": "user/gpg_keys"},
    {"method": "GET", "path": "user/gpg_keys/{id}"},
    {"method": "GET", "path": "user/installations"},
    {"method": "GET", "path": "user/installations/{id}/repositories"},
    {"method": "GET", "path": "user/interaction-limits"},
    {"method": "GET", "path": "user/issue-fields"},
    {"method": "GET", "path": "user/issue-types"},
    {"method": "GET", "path": "user/issues"},
    {"method": "GET", "path": "user/keys"},
    {"method": "GET", "path": "user/keys/{id}"},
    {"method": "GET", "path": "user/marketplace_purchases"},
    {"method": "GET", "path": "user/marketplace_purchases/stubbed"},
    {"method": "GET", "path": "user/memberships/orgs"},
    {"method": "GET", "path": "user/memberships/orgs/{id}"},
    {"method": "GET", "path": "user/migrations/**"},
    {"method": "GET", "path": "user/orgs"},
    {"method": "GET", "path": "user/packages/**"},
    {"method": "GET", "path": "user/public_emails"},
    {"method": "GET", "path": "user/repos"},
    {"method": "GET", "path": "user/repository_invitations"},
    {"method": "GET", "path": "user/social_accounts"},
    {"method": "GET", "path": "user/ssh_signing_keys"},
    {"method": "GET", "path": "user/ssh_signing_keys/{id}"},
    {"method": "GET", "path": "user/starred"},
    {"method": "GET", "path": "user/starred/{id}/{id}"},
    {"method": "GET", "path": "user/subscriptions"},
    {"method": "GET", "path": "user/teams"},
    {"method": "GET", "path": "user/{id}"},
    {"method": "GET", "path": "users"},
    {"method": "GET", "path": "users/{id}"},
    {"method": "POST", "path": "users/{id}/attestations/bulk-list"},
    {"method": "GET", "path": "users/{id}/attestations/{id}"},
    {"method": "GET", "path": "users/{id}/copilot-spaces/**"},
    {"method": "GET", "path": "users/{id}/docker/conflicts"},
    {"method": "GET", "path": "users/{id}/events"},
    {"method": "GET", "path": "users/{id}/events/orgs/{id}"},
    {"method": "GET", "path": "users/{id}/events/public"},
    {"method": "GET", "path": "users/{id}/followers"},
    {"method": "GET", "path": "users/{id}/following"},
    {"method": "GET", "path": "users/{id}/following/{id}"},
    {"method": "GET", "path": "users/{id}/gists"},
    {"method": "GET", "path": "users/{id}/gpg_keys"},
    {"method": "GET", "path": "users/{id}/hovercard"},
    {"method": "GET", "path": "users/{id}/installation"},
    {"method": "GET", "path": "users/{id}/keys"},
    {"method": "GET", "path": "users/{id}/orgs"},
    {"method": "GET", "path": "users/{id}/packages/**"},
    {"method": "GET", "path": "users/{id}/projectsV2/**"},
    {"method": "GET", "path": "users/{id}/received_events"},
    {"method": "GET", "path": "users/{id}/received_events/public"},
    {"method": "GET", "path": "users/{id}/repos"},
    {"method": "GET", "path": "users/{id}/settings/**"},
    {"method": "GET", "path": "users/{id}/social_accounts"},
    {"method": "GET", "path": "users/{id}/ssh_signing_keys"},
    {"method": "GET", "path": "users/{id}/starred"},
    {"method": "GET", "path": "users/{id}/subscriptions"},
    {"method": "GET", "path": "versions"},
    {"method": "GET", "path": "zen"},
    {"method": "POST", "path": "graphql", "when": {"graphql": "query"}}
  ],
  "deny": []
}
```

## Endpoints

The GitHub endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | advisories | read | security advisories | List global security advisories. |
| GET | advisories/{id} | read | security advisories | Get a global security advisory. |
| POST | agents/repos/{id}/{id}/automations | write | agent automations | Create an automation for a repository. |
| PATCH | agents/repos/{id}/{id}/automations/{id} | write | agent automations | Update an automation. |
| DELETE | agents/repos/{id}/{id}/automations/{id} | write | agent automations | Delete an automation. |
| POST | agents/repos/{id}/{id}/automations/{id}/tasks | write | agent automations | Run an automation. |
| PUT | agents/repos/{id}/{id}/pulls/{id}/agent-merge | write | pull requests | Update Agent Merge configuration for a pull request. |
| DELETE | agents/repos/{id}/{id}/pulls/{id}/agent-merge | write | pull requests | Disable Agent Merge for a pull request. |
| POST | agents/repos/{id}/{id}/tasks | write | agent tasks | Start a task. |
| GET | `agents/**` | read | agent automations | Read anything under agents (13 documented GET endpoints, all plain reads). |
| POST | app-manifests/{id}/conversions | write | apps | Create a GitHub App from a manifest. |
| GET | apps/{id} | read | apps | Get an app. |
| GET | codes_of_conduct | read | codes of conduct | Get all codes of conduct. |
| GET | codes_of_conduct/{id} | read | codes of conduct | Get a code of conduct. |
| POST | credentials/revoke | write | credentials | Revoke a list of credentials. |
| GET | emojis | read | emojis | Get emojis. |
| GET | events | read | activity | List public events. |
| GET | feeds | write | activity | Get feeds; kept out of read: returns private Atom feed URLs that carry the user's feed token. |
| GET | gists | read | gists | List gists for the authenticated user. |
| POST | gists | write | gists | Create a gist. |
| GET | gists/public | read | gists | List public gists. |
| GET | gists/starred | read | gists | List starred gists. |
| GET | gists/{id} | read | gists | Get a gist. |
| PATCH | gists/{id} | write | gists | Update a gist. |
| DELETE | gists/{id} | write | gists | Delete a gist. |
| GET | gists/{id}/comments | read | gists | List gist comments. |
| POST | gists/{id}/comments | write | gists | Create a gist comment. |
| GET | gists/{id}/comments/{id} | read | gists | Get a gist comment. |
| PATCH | gists/{id}/comments/{id} | write | gists | Update a gist comment. |
| DELETE | gists/{id}/comments/{id} | write | gists | Delete a gist comment. |
| GET | gists/{id}/commits | read | gists | List gist commits. |
| GET | gists/{id}/forks | read | gists | List gist forks. |
| POST | gists/{id}/forks | write | gists | Fork a gist. |
| GET | gists/{id}/star | read | gists | Check if a gist is starred. |
| PUT | gists/{id}/star | write | gists | Star a gist. |
| DELETE | gists/{id}/star | write | gists | Unstar a gist. |
| GET | gists/{id}/{id} | read | gists | Get a gist revision. |
| GET | gitignore/templates | read | gitignore | Get all gitignore templates. |
| GET | gitignore/templates/{id} | read | gitignore | Get a gitignore template. |
| GET | installation/repositories | read | apps | List repositories accessible to the app installation. |
| DELETE | installation/token | write | apps | Revoke an installation access token. |
| GET | issues | read | issues | List issues assigned to the authenticated user. |
| GET | licenses | read | licenses | Get all commonly used licenses. |
| GET | licenses/{id} | read | licenses | Get a license. |
| POST | markdown | read | markdown | Render a Markdown document. |
| POST | markdown/raw | read | markdown | Render a Markdown document in raw mode. |
| GET | meta | read | meta | Get GitHub meta information. |
| GET | networks/{id}/{id}/events | read | activity | List public events for a network of repositories. |
| GET | notifications | read | activity | List notifications for the authenticated user. |
| PUT | notifications | write | activity | Mark notifications as read. |
| GET | notifications/threads/{id} | read | activity | Get a thread. |
| PATCH | notifications/threads/{id} | write | activity | Mark a thread as read. |
| DELETE | notifications/threads/{id} | write | activity | Mark a thread as done. |
| GET | notifications/threads/{id}/subscription | read | activity | Get a thread subscription for the authenticated user. |
| PUT | notifications/threads/{id}/subscription | write | activity | Set a thread subscription. |
| DELETE | notifications/threads/{id}/subscription | write | activity | Delete a thread subscription. |
| GET | octocat | read | meta | Get Octocat. |
| PUT | organizations/{id}/actions/cache/retention-limit | write | actions | Set GitHub Actions cache retention limit for an organization. |
| PUT | organizations/{id}/actions/cache/storage-limit | write | actions | Set GitHub Actions cache storage limit for an organization. |
| POST | organizations/{id}/settings/billing/budgets | write | billing | Create a budget for an organization. |
| PATCH | organizations/{id}/settings/billing/budgets/{id} | write | billing | Update a budget for an organization. |
| DELETE | organizations/{id}/settings/billing/budgets/{id} | write | billing | Delete a budget for an organization. |
| GET | `organizations/**` | read | billing | Read anything under organizations (9 documented GET endpoints, all plain reads). |
| GET | orgs/{id} | read | organizations | Get an organization. |
| PATCH | orgs/{id} | write | organizations | Update an organization. |
| DELETE | orgs/{id} | write | organizations | Delete an organization. |
| POST | orgs/{id}/actions/hosted-runners | write | actions | Create a GitHub-hosted runner for an organization. |
| DELETE | orgs/{id}/actions/hosted-runners/images/custom/{id} | write | actions | Delete a custom image from the organization. |
| DELETE | orgs/{id}/actions/hosted-runners/images/custom/{id}/versions/{id} | write | actions | Delete an image version of custom image from the organization. |
| PATCH | orgs/{id}/actions/hosted-runners/{id} | write | actions | Update a GitHub-hosted runner for an organization. |
| DELETE | orgs/{id}/actions/hosted-runners/{id} | write | actions | Delete a GitHub-hosted runner for an organization. |
| POST | orgs/{id}/actions/oidc/customization/properties/repo | write | actions | Create an OIDC custom property inclusion for an organization. |
| DELETE | orgs/{id}/actions/oidc/customization/properties/repo/{id} | write | actions | Delete an OIDC custom property inclusion for an organization. |
| PUT | orgs/{id}/actions/oidc/customization/sub | write | actions | Set the customization template for an OIDC subject claim for an organization. |
| PUT | orgs/{id}/actions/permissions | write | actions | Set GitHub Actions permissions for an organization. |
| PUT | orgs/{id}/actions/permissions/artifact-and-log-retention | write | actions | Set artifact and log retention settings for an organization. |
| PUT | orgs/{id}/actions/permissions/fork-pr-contributor-approval | write | actions | Set fork PR contributor approval permissions for an organization. |
| PUT | orgs/{id}/actions/permissions/fork-pr-workflows-private-repos | write | actions | Set private repo fork PR workflow settings for an organization. |
| PUT | orgs/{id}/actions/permissions/repositories | write | actions | Set selected repositories enabled for GitHub Actions in an organization. |
| PUT | orgs/{id}/actions/permissions/repositories/{id} | write | actions | Enable a selected repository for GitHub Actions in an organization. |
| DELETE | orgs/{id}/actions/permissions/repositories/{id} | write | actions | Disable a selected repository for GitHub Actions in an organization. |
| PUT | orgs/{id}/actions/permissions/selected-actions | write | actions | Set allowed actions and reusable workflows for an organization. |
| PUT | orgs/{id}/actions/permissions/self-hosted-runners | write | actions | Set self-hosted runners settings for an organization. |
| PUT | orgs/{id}/actions/permissions/self-hosted-runners/repositories | write | actions | Set repositories allowed to use self-hosted runners in an organization. |
| PUT | orgs/{id}/actions/permissions/self-hosted-runners/repositories/{id} | write | actions | Add a repository to the list of repositories allowed to use self-hosted runners in an organization. |
| DELETE | orgs/{id}/actions/permissions/self-hosted-runners/repositories/{id} | write | actions | Remove a repository from the list of repositories allowed to use self-hosted runners in an organization. |
| PUT | orgs/{id}/actions/permissions/workflow | write | actions | Set default workflow permissions for an organization. |
| POST | orgs/{id}/actions/policies | write | actions | Create an organization Actions policy. |
| PUT | orgs/{id}/actions/policies/{id} | write | actions | Update an organization Actions policy. |
| DELETE | orgs/{id}/actions/policies/{id} | write | actions | Delete an organization Actions policy. |
| POST | orgs/{id}/actions/runner-groups | write | actions | Create a self-hosted runner group for an organization. |
| PATCH | orgs/{id}/actions/runner-groups/{id} | write | actions | Update a self-hosted runner group for an organization. |
| DELETE | orgs/{id}/actions/runner-groups/{id} | write | actions | Delete a self-hosted runner group from an organization. |
| PUT | orgs/{id}/actions/runner-groups/{id}/repositories | write | actions | Set repository access for a self-hosted runner group in an organization. |
| PUT | orgs/{id}/actions/runner-groups/{id}/repositories/{id} | write | actions | Add repository access to a self-hosted runner group in an organization. |
| DELETE | orgs/{id}/actions/runner-groups/{id}/repositories/{id} | write | actions | Remove repository access to a self-hosted runner group in an organization. |
| PUT | orgs/{id}/actions/runner-groups/{id}/runners | write | actions | Set self-hosted runners in a group for an organization. |
| PUT | orgs/{id}/actions/runner-groups/{id}/runners/{id} | write | actions | Add a self-hosted runner to a group for an organization. |
| DELETE | orgs/{id}/actions/runner-groups/{id}/runners/{id} | write | actions | Remove a self-hosted runner from a group for an organization. |
| POST | orgs/{id}/actions/runners/generate-jitconfig | write | actions | Create configuration for a just-in-time runner for an organization. |
| POST | orgs/{id}/actions/runners/registration-token | write | actions | Create a registration token for an organization. |
| POST | orgs/{id}/actions/runners/remove-token | write | actions | Create a remove token for an organization. |
| DELETE | orgs/{id}/actions/runners/{id} | write | actions | Delete a self-hosted runner from an organization. |
| POST | orgs/{id}/actions/runners/{id}/labels | write | actions | Add custom labels to a self-hosted runner for an organization. |
| PUT | orgs/{id}/actions/runners/{id}/labels | write | actions | Set custom labels for a self-hosted runner for an organization. |
| DELETE | orgs/{id}/actions/runners/{id}/labels | write | actions | Remove all custom labels from a self-hosted runner for an organization. |
| DELETE | orgs/{id}/actions/runners/{id}/labels/{id} | write | actions | Remove a custom label from a self-hosted runner for an organization. |
| PUT | orgs/{id}/actions/secrets/{id} | write | actions | Create or update an organization secret. |
| DELETE | orgs/{id}/actions/secrets/{id} | write | actions | Delete an organization secret. |
| PUT | orgs/{id}/actions/secrets/{id}/repositories | write | actions | Set selected repositories for an organization secret. |
| PUT | orgs/{id}/actions/secrets/{id}/repositories/{id} | write | actions | Add selected repository to an organization secret. |
| DELETE | orgs/{id}/actions/secrets/{id}/repositories/{id} | write | actions | Remove selected repository from an organization secret. |
| POST | orgs/{id}/actions/variables | write | actions | Create an organization variable. |
| PATCH | orgs/{id}/actions/variables/{id} | write | actions | Update an organization variable. |
| DELETE | orgs/{id}/actions/variables/{id} | write | actions | Delete an organization variable. |
| PUT | orgs/{id}/actions/variables/{id}/repositories | write | actions | Set selected repositories for an organization variable. |
| PUT | orgs/{id}/actions/variables/{id}/repositories/{id} | write | actions | Add selected repository to an organization variable. |
| DELETE | orgs/{id}/actions/variables/{id}/repositories/{id} | write | actions | Remove selected repository from an organization variable. |
| GET | `orgs/{id}/actions/**` | read | actions | Read anything under orgs/{id}/actions (43 documented GET endpoints, all plain reads). |
| PUT | orgs/{id}/agents/secrets/{id} | write | agents | Create or update an organization secret. |
| DELETE | orgs/{id}/agents/secrets/{id} | write | agents | Delete an organization secret. |
| PUT | orgs/{id}/agents/secrets/{id}/repositories | write | agents | Set selected repositories for an organization secret. |
| PUT | orgs/{id}/agents/secrets/{id}/repositories/{id} | write | agents | Add selected repository to an organization secret. |
| DELETE | orgs/{id}/agents/secrets/{id}/repositories/{id} | write | agents | Remove selected repository from an organization secret. |
| POST | orgs/{id}/agents/variables | write | agents | Create an organization variable. |
| PATCH | orgs/{id}/agents/variables/{id} | write | agents | Update an organization variable. |
| DELETE | orgs/{id}/agents/variables/{id} | write | agents | Delete an organization variable. |
| PUT | orgs/{id}/agents/variables/{id}/repositories | write | agents | Set selected repositories for an organization variable. |
| PUT | orgs/{id}/agents/variables/{id}/repositories/{id} | write | agents | Add selected repository to an organization variable. |
| DELETE | orgs/{id}/agents/variables/{id}/repositories/{id} | write | agents | Remove selected repository from an organization variable. |
| GET | `orgs/{id}/agents/**` | read | agents | Read anything under orgs/{id}/agents (7 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/artifacts/metadata/deployment-record | write | organizations | Create an artifact deployment record. |
| POST | orgs/{id}/artifacts/metadata/deployment-record/cluster/{id} | write | organizations | Set cluster deployment records. |
| POST | orgs/{id}/artifacts/metadata/deployment-record/cluster/{id}/jobs | write | organizations | Create a cluster deployment records job. |
| POST | orgs/{id}/artifacts/metadata/storage-record | write | organizations | Create artifact metadata storage record. |
| GET | `orgs/{id}/artifacts/**` | read | organizations | Read anything under orgs/{id}/artifacts (3 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/attestations/bulk-list | read | organizations | List attestations by bulk subject digests. |
| POST | orgs/{id}/attestations/delete-request | write | organizations | Delete attestations in bulk. |
| DELETE | orgs/{id}/attestations/digest/{id} | write | organizations | Delete attestations by subject digest. |
| GET | orgs/{id}/attestations/repositories | read | organizations | List attestation repositories. |
| GET | orgs/{id}/attestations/{id} | read | organizations | List attestations. |
| DELETE | orgs/{id}/attestations/{id} | write | organizations | Delete attestations by ID. |
| GET | orgs/{id}/blocks | read | organizations | List users blocked by an organization. |
| GET | orgs/{id}/blocks/{id} | read | organizations | Check if a user is blocked by an organization. |
| PUT | orgs/{id}/blocks/{id} | write | organizations | Block a user from an organization. |
| DELETE | orgs/{id}/blocks/{id} | write | organizations | Unblock a user from an organization. |
| GET | orgs/{id}/campaigns | read | campaigns | List campaigns for an organization. |
| POST | orgs/{id}/campaigns | write | campaigns | Create a campaign for an organization. |
| GET | orgs/{id}/campaigns/{id} | read | campaigns | Get a campaign for an organization. |
| PATCH | orgs/{id}/campaigns/{id} | write | campaigns | Update a campaign. |
| DELETE | orgs/{id}/campaigns/{id} | write | campaigns | Delete a campaign for an organization. |
| PATCH | orgs/{id}/code-scanning/ai-scan | write | code scanning | Update the AI Scan setting for an organization. |
| GET | `orgs/{id}/code-scanning/**` | read | code scanning | Read anything under orgs/{id}/code-scanning (2 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/code-security/configurations | write | code security | Create a code security configuration. |
| DELETE | orgs/{id}/code-security/configurations/detach | write | code security | Detach configurations from repositories. |
| PATCH | orgs/{id}/code-security/configurations/{id} | write | code security | Update a code security configuration. |
| DELETE | orgs/{id}/code-security/configurations/{id} | write | code security | Delete a code security configuration. |
| POST | orgs/{id}/code-security/configurations/{id}/attach | write | code security | Attach a configuration to repositories. |
| PUT | orgs/{id}/code-security/configurations/{id}/defaults | write | code security | Set a code security configuration as a default for an organization. |
| GET | `orgs/{id}/code-security/**` | read | code security | Read anything under orgs/{id}/code-security (4 documented GET endpoints, all plain reads). |
| PUT | orgs/{id}/codespaces/access | write | codespaces | Manage access control for organization codespaces. |
| POST | orgs/{id}/codespaces/access/selected_users | write | codespaces | Add users to Codespaces access for an organization. |
| DELETE | orgs/{id}/codespaces/access/selected_users | write | codespaces | Remove users from Codespaces access for an organization. |
| PUT | orgs/{id}/codespaces/secrets/{id} | write | codespaces | Create or update an organization secret. |
| DELETE | orgs/{id}/codespaces/secrets/{id} | write | codespaces | Delete an organization secret. |
| PUT | orgs/{id}/codespaces/secrets/{id}/repositories | write | codespaces | Set selected repositories for an organization secret. |
| PUT | orgs/{id}/codespaces/secrets/{id}/repositories/{id} | write | codespaces | Add selected repository to an organization secret. |
| DELETE | orgs/{id}/codespaces/secrets/{id}/repositories/{id} | write | codespaces | Remove selected repository from an organization secret. |
| GET | `orgs/{id}/codespaces/**` | read | codespaces | Read anything under orgs/{id}/codespaces (5 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/copilot-spaces | write | copilot spaces | Create an organization Copilot Space. |
| PUT | orgs/{id}/copilot-spaces/{id} | write | copilot spaces | Set an organization Copilot Space. |
| DELETE | orgs/{id}/copilot-spaces/{id} | write | copilot spaces | Delete an organization Copilot Space. |
| POST | orgs/{id}/copilot-spaces/{id}/collaborators | write | copilot spaces | Add a collaborator to an organization Copilot Space. |
| PUT | orgs/{id}/copilot-spaces/{id}/collaborators/{id}/{id} | write | copilot spaces | Set a collaborator role for an organization Copilot Space. |
| DELETE | orgs/{id}/copilot-spaces/{id}/collaborators/{id}/{id} | write | copilot spaces | Remove a collaborator from an organization Copilot Space. |
| POST | orgs/{id}/copilot-spaces/{id}/resources | write | copilot spaces | Create a resource for an organization Copilot Space. |
| PUT | orgs/{id}/copilot-spaces/{id}/resources/{id} | write | copilot spaces | Set a resource for an organization Copilot Space. |
| DELETE | orgs/{id}/copilot-spaces/{id}/resources/{id} | write | copilot spaces | Delete a resource from an organization Copilot Space. |
| GET | `orgs/{id}/copilot-spaces/**` | read | copilot spaces | Read anything under orgs/{id}/copilot-spaces (5 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/copilot/billing/selected_teams | write | copilot | Add teams to the Copilot subscription for an organization. |
| DELETE | orgs/{id}/copilot/billing/selected_teams | write | copilot | Remove teams from the Copilot subscription for an organization. |
| POST | orgs/{id}/copilot/billing/selected_users | write | copilot | Add users to the Copilot subscription for an organization. |
| DELETE | orgs/{id}/copilot/billing/selected_users | write | copilot | Remove users from the Copilot subscription for an organization. |
| PUT | orgs/{id}/copilot/code-review/runner | write | copilot | Set the Copilot code review runner configuration for an organization. |
| PATCH | orgs/{id}/copilot/code-review/settings | write | copilot | Update Copilot code review settings for an organization. |
| PUT | orgs/{id}/copilot/coding-agent/permissions | write | copilot | Set Copilot cloud agent permissions for an organization. |
| PUT | orgs/{id}/copilot/coding-agent/permissions/repositories | write | copilot | Set selected repositories for Copilot cloud agent in an organization. |
| PUT | orgs/{id}/copilot/coding-agent/permissions/repositories/{id} | write | copilot | Enable a repository for Copilot cloud agent in an organization. |
| DELETE | orgs/{id}/copilot/coding-agent/permissions/repositories/{id} | write | copilot | Disable a repository for Copilot cloud agent in an organization. |
| PUT | orgs/{id}/copilot/content_exclusion | write | copilot | Set Copilot content exclusion rules for an organization. |
| PUT | orgs/{id}/copilot/policies/code-review | write | copilot | Set the Copilot code review policy for an organization. |
| GET | `orgs/{id}/copilot/**` | read | copilot | Read anything under orgs/{id}/copilot (14 documented GET endpoints, all plain reads). |
| PATCH | orgs/{id}/dependabot/repository-access | write | dependabot | Updates Dependabot's repository access list for an organization. |
| PUT | orgs/{id}/dependabot/repository-access/default-level | write | dependabot | Set the default repository access level for Dependabot. |
| PUT | orgs/{id}/dependabot/secrets/{id} | write | dependabot | Create or update an organization secret. |
| DELETE | orgs/{id}/dependabot/secrets/{id} | write | dependabot | Delete an organization secret. |
| PUT | orgs/{id}/dependabot/secrets/{id}/repositories | write | dependabot | Set selected repositories for an organization secret. |
| PUT | orgs/{id}/dependabot/secrets/{id}/repositories/{id} | write | dependabot | Add selected repository to an organization secret. |
| DELETE | orgs/{id}/dependabot/secrets/{id}/repositories/{id} | write | dependabot | Remove selected repository from an organization secret. |
| GET | `orgs/{id}/dependabot/**` | read | dependabot | Read anything under orgs/{id}/dependabot (6 documented GET endpoints, all plain reads). |
| GET | orgs/{id}/docker/conflicts | read | packages | Get list of conflicting packages during Docker migration for organization. |
| GET | orgs/{id}/events | read | activity | List public organization events. |
| GET | orgs/{id}/failed_invitations | read | organizations | List failed organization invitations. |
| GET | orgs/{id}/hooks | write | organizations | List organization webhooks; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| POST | orgs/{id}/hooks | write | organizations | Create an organization webhook. |
| GET | orgs/{id}/hooks/{id} | write | organizations | Get an organization webhook; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| PATCH | orgs/{id}/hooks/{id} | write | organizations | Update an organization webhook. |
| DELETE | orgs/{id}/hooks/{id} | write | organizations | Delete an organization webhook. |
| GET | orgs/{id}/hooks/{id}/config | write | organizations | Get a webhook configuration for an organization; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| PATCH | orgs/{id}/hooks/{id}/config | write | organizations | Update a webhook configuration for an organization. |
| GET | orgs/{id}/hooks/{id}/deliveries | write | organizations | List deliveries for an organization webhook; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| GET | orgs/{id}/hooks/{id}/deliveries/{id} | write | organizations | Get a webhook delivery for an organization webhook; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| POST | orgs/{id}/hooks/{id}/deliveries/{id}/attempts | write | organizations | Redeliver a delivery for an organization webhook. |
| POST | orgs/{id}/hooks/{id}/pings | write | organizations | Ping an organization webhook. |
| GET | `orgs/{id}/insights/**` | read | organizations | Read anything under orgs/{id}/insights (9 documented GET endpoints, all plain reads). |
| GET | orgs/{id}/installation | read | apps | Get an organization installation for the authenticated app. |
| GET | orgs/{id}/installations | read | organizations | List app installations for an organization. |
| GET | orgs/{id}/interaction-limits | read | interactions | Get interaction restrictions for an organization. |
| PUT | orgs/{id}/interaction-limits | write | interactions | Set interaction restrictions for an organization. |
| DELETE | orgs/{id}/interaction-limits | write | interactions | Remove interaction restrictions for an organization. |
| GET | orgs/{id}/interaction-limits/pulls/creation-cap | read | interactions | Get pull request creation cap for an org. |
| PATCH | orgs/{id}/interaction-limits/pulls/creation-cap | write | interactions | Update pull request creation cap for an org. |
| GET | orgs/{id}/invitations | read | organizations | List pending organization invitations. |
| POST | orgs/{id}/invitations | write | organizations | Create an organization invitation. |
| DELETE | orgs/{id}/invitations/{id} | write | organizations | Cancel an organization invitation. |
| GET | orgs/{id}/invitations/{id}/teams | read | organizations | List organization invitation teams. |
| GET | orgs/{id}/issue-fields | read | organizations | List issue fields for an organization. |
| POST | orgs/{id}/issue-fields | write | organizations | Create issue field for an organization. |
| PATCH | orgs/{id}/issue-fields/{id} | write | organizations | Update issue field for an organization. |
| DELETE | orgs/{id}/issue-fields/{id} | write | organizations | Delete issue field for an organization. |
| GET | orgs/{id}/issue-types | read | organizations | List issue types for an organization. |
| POST | orgs/{id}/issue-types | write | organizations | Create issue type for an organization. |
| PUT | orgs/{id}/issue-types/{id} | write | organizations | Update issue type for an organization. |
| DELETE | orgs/{id}/issue-types/{id} | write | organizations | Delete issue type for an organization. |
| GET | orgs/{id}/issues | read | issues | List organization issues assigned to the authenticated user. |
| GET | orgs/{id}/members | read | organizations | List organization members. |
| GET | orgs/{id}/members/{id} | read | organizations | Check organization membership for a user. |
| DELETE | orgs/{id}/members/{id} | write | organizations | Remove an organization member. |
| GET | orgs/{id}/members/{id}/codespaces | read | codespaces | List codespaces for a user in organization. |
| DELETE | orgs/{id}/members/{id}/codespaces/{id} | write | codespaces | Delete a codespace from the organization. |
| POST | orgs/{id}/members/{id}/codespaces/{id}/stop | write | codespaces | Stop a codespace for an organization user. |
| GET | orgs/{id}/members/{id}/copilot | read | copilot | Get Copilot seat assignment details for a user. |
| GET | orgs/{id}/memberships/{id} | read | organizations | Get organization membership for a user. |
| PUT | orgs/{id}/memberships/{id} | write | organizations | Set organization membership for a user. |
| DELETE | orgs/{id}/memberships/{id} | write | organizations | Remove organization membership for a user. |
| POST | orgs/{id}/migrations | write | migrations | Start an organization migration. |
| DELETE | orgs/{id}/migrations/{id}/archive | write | migrations | Delete an organization migration archive. |
| DELETE | orgs/{id}/migrations/{id}/repos/{id}/lock | write | migrations | Unlock an organization repository. |
| GET | `orgs/{id}/migrations/**` | read | migrations | Read anything under orgs/{id}/migrations (4 documented GET endpoints, all plain reads). |
| DELETE | orgs/{id}/organization-roles/teams/{id} | write | organizations | Remove all organization roles for a team. |
| PUT | orgs/{id}/organization-roles/teams/{id}/{id} | write | organizations | Assign an organization role to a team. |
| DELETE | orgs/{id}/organization-roles/teams/{id}/{id} | write | organizations | Remove an organization role from a team. |
| DELETE | orgs/{id}/organization-roles/users/{id} | write | organizations | Remove all organization roles for a user. |
| PUT | orgs/{id}/organization-roles/users/{id}/{id} | write | organizations | Assign an organization role to a user. |
| DELETE | orgs/{id}/organization-roles/users/{id}/{id} | write | organizations | Remove an organization role from a user. |
| GET | `orgs/{id}/organization-roles/**` | read | organizations | Read anything under orgs/{id}/organization-roles (4 documented GET endpoints, all plain reads). |
| GET | orgs/{id}/outside_collaborators | read | organizations | List outside collaborators for an organization. |
| PUT | orgs/{id}/outside_collaborators/{id} | write | organizations | Convert an organization member to outside collaborator. |
| DELETE | orgs/{id}/outside_collaborators/{id} | write | organizations | Remove outside collaborator from an organization. |
| DELETE | orgs/{id}/packages/{id}/{id} | write | packages | Delete a package for an organization. |
| POST | orgs/{id}/packages/{id}/{id}/restore | write | packages | Restore a package for an organization. |
| DELETE | orgs/{id}/packages/{id}/{id}/versions/{id} | write | packages | Delete package version for an organization. |
| POST | orgs/{id}/packages/{id}/{id}/versions/{id}/restore | write | packages | Restore package version for an organization. |
| GET | `orgs/{id}/packages/**` | read | packages | Read anything under orgs/{id}/packages (4 documented GET endpoints, all plain reads). |
| GET | orgs/{id}/personal-access-token-requests | read | organizations | List requests to access organization resources with fine-grained personal access tokens. |
| POST | orgs/{id}/personal-access-token-requests | write | organizations | Review requests to access organization resources with fine-grained personal access tokens. |
| POST | orgs/{id}/personal-access-token-requests/{id} | write | organizations | Review a request to access organization resources with a fine-grained personal access token. |
| GET | orgs/{id}/personal-access-token-requests/{id}/repositories | read | organizations | List repositories requested to be accessed by a fine-grained personal access token. |
| GET | orgs/{id}/personal-access-tokens | read | organizations | List fine-grained personal access tokens with access to organization resources. |
| POST | orgs/{id}/personal-access-tokens | write | organizations | Update the access to organization resources via fine-grained personal access tokens. |
| POST | orgs/{id}/personal-access-tokens/{id} | write | organizations | Update the access a fine-grained personal access token has to organization resources. |
| GET | orgs/{id}/personal-access-tokens/{id}/repositories | read | organizations | List repositories a fine-grained personal access token has access to. |
| POST | orgs/{id}/private-registries | write | private registries | Create a private registry for an organization. |
| PATCH | orgs/{id}/private-registries/{id} | write | private registries | Update a private registry for an organization. |
| DELETE | orgs/{id}/private-registries/{id} | write | private registries | Delete a private registry for an organization. |
| GET | `orgs/{id}/private-registries/**` | read | private registries | Read anything under orgs/{id}/private-registries (3 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/projectsV2/{id}/drafts | write | projects | Create draft item for organization owned project. |
| POST | orgs/{id}/projectsV2/{id}/fields | write | projects | Add a field to an organization-owned project. |
| POST | orgs/{id}/projectsV2/{id}/items | write | projects | Add item to organization owned project. |
| PATCH | orgs/{id}/projectsV2/{id}/items/{id} | write | projects | Update project item for organization. |
| DELETE | orgs/{id}/projectsV2/{id}/items/{id} | write | projects | Delete project item for organization. |
| POST | orgs/{id}/projectsV2/{id}/views | write | projects | Create a view for an organization-owned project. |
| GET | `orgs/{id}/projectsV2/**` | read | projects | Read anything under orgs/{id}/projectsV2 (7 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/properties/installations | write | organizations | Register an app installation for external custom properties. |
| PATCH | orgs/{id}/properties/installations/values | write | organizations | Create or update external custom property values for organization repositories. |
| PATCH | orgs/{id}/properties/installations/values/{id} | write | organizations | Create or update external custom property values for a property across organization repositories. |
| DELETE | orgs/{id}/properties/installations/values/{id} | write | organizations | Remove all external custom property values for a property across all organization repositories. |
| PATCH | orgs/{id}/properties/schema | write | organizations | Create or update custom properties for an organization. |
| PUT | orgs/{id}/properties/schema/{id} | write | organizations | Create or update a custom property for an organization. |
| DELETE | orgs/{id}/properties/schema/{id} | write | organizations | Remove a custom property for an organization. |
| PATCH | orgs/{id}/properties/values | write | organizations | Create or update custom property values for organization repositories. |
| GET | `orgs/{id}/properties/**` | read | organizations | Read anything under orgs/{id}/properties (5 documented GET endpoints, all plain reads). |
| GET | orgs/{id}/public_members | read | organizations | List public organization members. |
| GET | orgs/{id}/public_members/{id} | read | organizations | Check public organization membership for a user. |
| PUT | orgs/{id}/public_members/{id} | write | organizations | Set public organization membership for the authenticated user. |
| DELETE | orgs/{id}/public_members/{id} | write | organizations | Remove public organization membership for the authenticated user. |
| GET | orgs/{id}/repos | read | repositories | List organization repositories. |
| POST | orgs/{id}/repos | write | repositories | Create an organization repository. |
| POST | orgs/{id}/rulesets | write | organizations | Create an organization repository ruleset. |
| PUT | orgs/{id}/rulesets/{id} | write | organizations | Update an organization repository ruleset. |
| DELETE | orgs/{id}/rulesets/{id} | write | organizations | Delete an organization repository ruleset. |
| GET | `orgs/{id}/rulesets/**` | read | organizations | Read anything under orgs/{id}/rulesets (6 documented GET endpoints, all plain reads). |
| GET | orgs/{id}/secret-scanning/alerts | write | secret scanning | List secret scanning alerts for an organization; kept out of read: returns the leaked secret values found by secret scanning. |
| GET | orgs/{id}/secret-scanning/custom-patterns | read | secret scanning | List organization custom patterns. |
| POST | orgs/{id}/secret-scanning/custom-patterns | write | secret scanning | Bulk create organization custom patterns. |
| DELETE | orgs/{id}/secret-scanning/custom-patterns | write | secret scanning | Bulk delete organization custom patterns. |
| PATCH | orgs/{id}/secret-scanning/custom-patterns/{id} | write | secret scanning | Update an organization custom pattern. |
| GET | orgs/{id}/secret-scanning/pattern-configurations | read | secret scanning | List organization pattern configurations. |
| PATCH | orgs/{id}/secret-scanning/pattern-configurations | write | secret scanning | Update organization pattern configurations. |
| GET | orgs/{id}/security-advisories | read | security advisories | List repository security advisories for an organization. |
| GET | orgs/{id}/security-managers | read | organizations | List security manager teams. |
| PUT | orgs/{id}/security-managers/teams/{id} | write | organizations | Add a security manager team. |
| DELETE | orgs/{id}/security-managers/teams/{id} | write | organizations | Remove a security manager team. |
| PUT | orgs/{id}/settings/immutable-releases | write | organizations | Set immutable releases settings for an organization. |
| PUT | orgs/{id}/settings/immutable-releases/repositories | write | organizations | Set selected repositories for immutable releases enforcement. |
| PUT | orgs/{id}/settings/immutable-releases/repositories/{id} | write | organizations | Enable a selected repository for immutable releases in an organization. |
| DELETE | orgs/{id}/settings/immutable-releases/repositories/{id} | write | organizations | Disable a selected repository for immutable releases in an organization. |
| POST | orgs/{id}/settings/network-configurations | write | organizations | Create a hosted compute network configuration for an organization. |
| PATCH | orgs/{id}/settings/network-configurations/{id} | write | organizations | Update a hosted compute network configuration for an organization. |
| DELETE | orgs/{id}/settings/network-configurations/{id} | write | organizations | Delete a hosted compute network configuration from an organization. |
| GET | `orgs/{id}/settings/**` | read | organizations | Read anything under orgs/{id}/settings (5 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/teams | write | teams | Create a team. |
| PATCH | orgs/{id}/teams/{id} | write | teams | Update a team. |
| DELETE | orgs/{id}/teams/{id} | write | teams | Delete a team. |
| PUT | orgs/{id}/teams/{id}/copilot/customizations | write | copilot | Set Copilot customizations for a team. |
| DELETE | orgs/{id}/teams/{id}/copilot/customizations | write | copilot | Delete Copilot customizations for a team. |
| PUT | orgs/{id}/teams/{id}/memberships/{id} | write | teams | Add or update team membership for a user. |
| DELETE | orgs/{id}/teams/{id}/memberships/{id} | write | teams | Remove team membership for a user. |
| PUT | orgs/{id}/teams/{id}/repos/{id}/{id} | write | teams | Add or update team repository permissions. |
| DELETE | orgs/{id}/teams/{id}/repos/{id}/{id} | write | teams | Remove a repository from a team. |
| GET | `orgs/{id}/teams/**` | read | teams | Read anything under orgs/{id}/teams (9 documented GET endpoints, all plain reads). |
| POST | orgs/{id}/{id}/{id} | write | organizations | Enable or disable a security feature for an organization. |
| GET | rate_limit | read | rate limit | Get rate limit status for the authenticated user. |
| GET | repos/{id}/{id} | read | repositories | Get a repository. |
| PATCH | repos/{id}/{id} | write | repositories | Update a repository. |
| DELETE | repos/{id}/{id} | write | repositories | Delete a repository. |
| GET | repos/{id}/{id}/actions/artifacts | read | actions | List artifacts for a repository. |
| GET | repos/{id}/{id}/actions/artifacts/{id} | read | actions | Get an artifact. |
| DELETE | repos/{id}/{id}/actions/artifacts/{id} | write | actions | Delete an artifact. |
| GET | repos/{id}/{id}/actions/artifacts/{id}/{id} | read | actions | Download an artifact. |
| PUT | repos/{id}/{id}/actions/cache/retention-limit | write | actions | Set GitHub Actions cache retention limit for a repository. |
| PUT | repos/{id}/{id}/actions/cache/storage-limit | write | actions | Set GitHub Actions cache storage limit for a repository. |
| GET | `repos/{id}/{id}/actions/cache/**` | read | actions | Read anything under repos/{id}/{id}/actions/cache (3 documented GET endpoints, all plain reads). |
| DELETE | repos/{id}/{id}/actions/caches | write | actions | Delete GitHub Actions caches for a repository (using a cache key). |
| DELETE | repos/{id}/{id}/actions/caches/{id} | write | actions | Delete a GitHub Actions cache for a repository (using a cache ID). |
| GET | `repos/{id}/{id}/actions/caches/**` | read | actions | Read anything under repos/{id}/{id}/actions/caches (1 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/actions/concurrency_groups | read | actions | List concurrency groups for a repository. |
| GET | repos/{id}/{id}/actions/concurrency_groups/{id} | read | actions | Get a concurrency group for a repository. |
| GET | repos/{id}/{id}/actions/jobs/{id} | read | actions | Get a job for a workflow run. |
| GET | repos/{id}/{id}/actions/jobs/{id}/logs | read | actions | Download job logs for a workflow run. |
| POST | repos/{id}/{id}/actions/jobs/{id}/rerun | write | actions | Re-run a job from a workflow run. |
| GET | repos/{id}/{id}/actions/jobs/{id}/steps/{id}/logs | read | actions | Download step logs for a workflow run job. |
| GET | repos/{id}/{id}/actions/oidc/customization/sub | read | actions | Get the customization template for an OIDC subject claim for a repository. |
| PUT | repos/{id}/{id}/actions/oidc/customization/sub | write | actions | Set the customization template for an OIDC subject claim for a repository. |
| GET | repos/{id}/{id}/actions/organization-secrets | read | actions | List repository organization secrets. |
| GET | repos/{id}/{id}/actions/organization-variables | read | actions | List repository organization variables. |
| PUT | repos/{id}/{id}/actions/permissions | write | actions | Set GitHub Actions permissions for a repository. |
| PUT | repos/{id}/{id}/actions/permissions/access | write | actions | Set the level of access for workflows outside of the repository. |
| PUT | repos/{id}/{id}/actions/permissions/artifact-and-log-retention | write | actions | Set artifact and log retention settings for a repository. |
| PUT | repos/{id}/{id}/actions/permissions/fork-pr-contributor-approval | write | actions | Set fork PR contributor approval permissions for a repository. |
| PUT | repos/{id}/{id}/actions/permissions/fork-pr-workflows-private-repos | write | actions | Set private repo fork PR workflow settings for a repository. |
| PUT | repos/{id}/{id}/actions/permissions/selected-actions | write | actions | Set allowed actions and reusable workflows for a repository. |
| PUT | repos/{id}/{id}/actions/permissions/workflow | write | actions | Set default workflow permissions for a repository. |
| GET | `repos/{id}/{id}/actions/permissions/**` | read | actions | Read anything under repos/{id}/{id}/actions/permissions (7 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/actions/policies | read | actions | List repository Actions policies. |
| POST | repos/{id}/{id}/actions/policies | write | actions | Create a repository Actions policy. |
| GET | repos/{id}/{id}/actions/policies/{id} | read | actions | Get a repository Actions policy. |
| PUT | repos/{id}/{id}/actions/policies/{id} | write | actions | Update a repository Actions policy. |
| DELETE | repos/{id}/{id}/actions/policies/{id} | write | actions | Delete a repository Actions policy. |
| POST | repos/{id}/{id}/actions/runners/generate-jitconfig | write | actions | Create configuration for a just-in-time runner for a repository. |
| POST | repos/{id}/{id}/actions/runners/registration-token | write | actions | Create a registration token for a repository. |
| POST | repos/{id}/{id}/actions/runners/remove-token | write | actions | Create a remove token for a repository. |
| DELETE | repos/{id}/{id}/actions/runners/{id} | write | actions | Delete a self-hosted runner from a repository. |
| POST | repos/{id}/{id}/actions/runners/{id}/labels | write | actions | Add custom labels to a self-hosted runner for a repository. |
| PUT | repos/{id}/{id}/actions/runners/{id}/labels | write | actions | Set custom labels for a self-hosted runner for a repository. |
| DELETE | repos/{id}/{id}/actions/runners/{id}/labels | write | actions | Remove all custom labels from a self-hosted runner for a repository. |
| DELETE | repos/{id}/{id}/actions/runners/{id}/labels/{id} | write | actions | Remove a custom label from a self-hosted runner for a repository. |
| GET | `repos/{id}/{id}/actions/runners/**` | read | actions | Read anything under repos/{id}/{id}/actions/runners (5 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/actions/runs | read | actions | List workflow runs for a repository. |
| GET | repos/{id}/{id}/actions/runs/{id} | read | actions | Get a workflow run. |
| DELETE | repos/{id}/{id}/actions/runs/{id} | write | actions | Delete a workflow run. |
| GET | repos/{id}/{id}/actions/runs/{id}/approvals | read | actions | Get the review history for a workflow run. |
| POST | repos/{id}/{id}/actions/runs/{id}/approve | write | actions | Approve a workflow run for a fork pull request. |
| GET | repos/{id}/{id}/actions/runs/{id}/artifacts | read | actions | List workflow run artifacts. |
| GET | repos/{id}/{id}/actions/runs/{id}/attempts/{id} | read | actions | Get a workflow run attempt. |
| GET | repos/{id}/{id}/actions/runs/{id}/attempts/{id}/jobs | read | actions | List jobs for a workflow run attempt. |
| GET | repos/{id}/{id}/actions/runs/{id}/attempts/{id}/logs | read | actions | Download workflow run attempt logs. |
| POST | repos/{id}/{id}/actions/runs/{id}/cancel | write | actions | Cancel a workflow run. |
| GET | repos/{id}/{id}/actions/runs/{id}/concurrency_groups | read | actions | List concurrency groups for a workflow run. |
| POST | repos/{id}/{id}/actions/runs/{id}/deployment_protection_rule | write | actions | Review custom deployment protection rules for a workflow run. |
| POST | repos/{id}/{id}/actions/runs/{id}/force-cancel | write | actions | Force cancel a workflow run. |
| GET | repos/{id}/{id}/actions/runs/{id}/jobs | read | actions | List jobs for a workflow run. |
| GET | repos/{id}/{id}/actions/runs/{id}/logs | read | actions | Download workflow run logs. |
| DELETE | repos/{id}/{id}/actions/runs/{id}/logs | write | actions | Delete workflow run logs. |
| GET | repos/{id}/{id}/actions/runs/{id}/pending_deployments | read | actions | Get pending deployments for a workflow run. |
| POST | repos/{id}/{id}/actions/runs/{id}/pending_deployments | write | actions | Review pending deployments for a workflow run. |
| POST | repos/{id}/{id}/actions/runs/{id}/rerun | write | actions | Re-run a workflow. |
| POST | repos/{id}/{id}/actions/runs/{id}/rerun-failed-jobs | write | actions | Re-run failed jobs from a workflow run. |
| GET | repos/{id}/{id}/actions/runs/{id}/timing | read | actions | Get workflow run usage. |
| PUT | repos/{id}/{id}/actions/secrets/{id} | write | actions | Create or update a repository secret. |
| DELETE | repos/{id}/{id}/actions/secrets/{id} | write | actions | Delete a repository secret. |
| GET | `repos/{id}/{id}/actions/secrets/**` | read | actions | Read anything under repos/{id}/{id}/actions/secrets (3 documented GET endpoints, all plain reads). |
| POST | repos/{id}/{id}/actions/variables | write | actions | Create a repository variable. |
| PATCH | repos/{id}/{id}/actions/variables/{id} | write | actions | Update a repository variable. |
| DELETE | repos/{id}/{id}/actions/variables/{id} | write | actions | Delete a repository variable. |
| GET | `repos/{id}/{id}/actions/variables/**` | read | actions | Read anything under repos/{id}/{id}/actions/variables (2 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/actions/workflows | read | actions | List repository workflows. |
| GET | repos/{id}/{id}/actions/workflows/{id} | read | actions | Get a workflow. |
| PUT | repos/{id}/{id}/actions/workflows/{id}/disable | write | actions | Disable a workflow. |
| POST | repos/{id}/{id}/actions/workflows/{id}/dispatches | write | actions | Create a workflow dispatch event. |
| PUT | repos/{id}/{id}/actions/workflows/{id}/enable | write | actions | Enable a workflow. |
| GET | repos/{id}/{id}/actions/workflows/{id}/runs | read | actions | List workflow runs for a workflow. |
| GET | repos/{id}/{id}/actions/workflows/{id}/timing | read | actions | Get workflow usage. |
| GET | repos/{id}/{id}/activity | read | repositories | List repository activities. |
| PUT | repos/{id}/{id}/agents/secrets/{id} | write | agents | Create or update a repository secret. |
| DELETE | repos/{id}/{id}/agents/secrets/{id} | write | agents | Delete a repository secret. |
| POST | repos/{id}/{id}/agents/variables | write | agents | Create a repository variable. |
| PATCH | repos/{id}/{id}/agents/variables/{id} | write | agents | Update a repository variable. |
| DELETE | repos/{id}/{id}/agents/variables/{id} | write | agents | Delete a repository variable. |
| GET | `repos/{id}/{id}/agents/**` | read | agents | Read anything under repos/{id}/{id}/agents (7 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/assignees | read | issues | List assignees. |
| GET | repos/{id}/{id}/assignees/{id} | read | issues | Check if a user can be assigned. |
| POST | repos/{id}/{id}/attestations | write | repositories | Create an attestation. |
| GET | repos/{id}/{id}/attestations/{id} | read | repositories | List attestations. |
| GET | repos/{id}/{id}/autolinks | read | repositories | Get all autolinks of a repository. |
| POST | repos/{id}/{id}/autolinks | write | repositories | Create an autolink reference for a repository. |
| GET | repos/{id}/{id}/autolinks/{id} | read | repositories | Get an autolink reference of a repository. |
| DELETE | repos/{id}/{id}/autolinks/{id} | write | repositories | Delete an autolink reference from a repository. |
| GET | repos/{id}/{id}/automated-security-fixes | read | repositories | Check if Dependabot security updates are enabled for a repository. |
| PUT | repos/{id}/{id}/automated-security-fixes | write | repositories | Enable Dependabot security updates. |
| DELETE | repos/{id}/{id}/automated-security-fixes | write | repositories | Disable Dependabot security updates. |
| PUT | repos/{id}/{id}/branches/{id}/protection | write | branches | Update branch protection. |
| DELETE | repos/{id}/{id}/branches/{id}/protection | write | branches | Delete branch protection. |
| POST | repos/{id}/{id}/branches/{id}/protection/enforce_admins | write | branches | Set admin branch protection. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/enforce_admins | write | branches | Delete admin branch protection. |
| PATCH | repos/{id}/{id}/branches/{id}/protection/required_pull_request_reviews | write | branches | Update pull request review protection. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/required_pull_request_reviews | write | branches | Delete pull request review protection. |
| POST | repos/{id}/{id}/branches/{id}/protection/required_signatures | write | branches | Create commit signature protection. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/required_signatures | write | branches | Delete commit signature protection. |
| PATCH | repos/{id}/{id}/branches/{id}/protection/required_status_checks | write | branches | Update status check protection. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/required_status_checks | write | branches | Remove status check protection. |
| POST | repos/{id}/{id}/branches/{id}/protection/required_status_checks/contexts | write | branches | Add status check contexts. |
| PUT | repos/{id}/{id}/branches/{id}/protection/required_status_checks/contexts | write | branches | Set status check contexts. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/required_status_checks/contexts | write | branches | Remove status check contexts. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/restrictions | write | branches | Delete access restrictions. |
| POST | repos/{id}/{id}/branches/{id}/protection/restrictions/apps | write | branches | Add app access restrictions. |
| PUT | repos/{id}/{id}/branches/{id}/protection/restrictions/apps | write | branches | Set app access restrictions. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/restrictions/apps | write | branches | Remove app access restrictions. |
| POST | repos/{id}/{id}/branches/{id}/protection/restrictions/teams | write | branches | Add team access restrictions. |
| PUT | repos/{id}/{id}/branches/{id}/protection/restrictions/teams | write | branches | Set team access restrictions. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/restrictions/teams | write | branches | Remove team access restrictions. |
| POST | repos/{id}/{id}/branches/{id}/protection/restrictions/users | write | branches | Add user access restrictions. |
| PUT | repos/{id}/{id}/branches/{id}/protection/restrictions/users | write | branches | Set user access restrictions. |
| DELETE | repos/{id}/{id}/branches/{id}/protection/restrictions/users | write | branches | Remove user access restrictions. |
| POST | repos/{id}/{id}/branches/{id}/rename | write | branches | Rename a branch. |
| GET | `repos/{id}/{id}/branches/**` | read | branches | Read anything under repos/{id}/{id}/branches (12 documented GET endpoints, all plain reads). |
| POST | repos/{id}/{id}/check-runs | write | checks | Create a check run. |
| GET | repos/{id}/{id}/check-runs/{id} | read | checks | Get a check run. |
| PATCH | repos/{id}/{id}/check-runs/{id} | write | checks | Update a check run. |
| GET | repos/{id}/{id}/check-runs/{id}/annotations | read | checks | List check run annotations. |
| POST | repos/{id}/{id}/check-runs/{id}/rerequest | write | checks | Rerequest a check run. |
| POST | repos/{id}/{id}/check-suites | write | checks | Create a check suite. |
| PATCH | repos/{id}/{id}/check-suites/preferences | write | checks | Update repository preferences for check suites. |
| GET | repos/{id}/{id}/check-suites/{id} | read | checks | Get a check suite. |
| GET | repos/{id}/{id}/check-suites/{id}/check-runs | read | checks | List check runs in a check suite. |
| POST | repos/{id}/{id}/check-suites/{id}/rerequest | write | checks | Rerequest a check suite. |
| PATCH | repos/{id}/{id}/code-quality/setup | write | code quality | Update a code quality setup configuration. |
| GET | `repos/{id}/{id}/code-quality/**` | read | code quality | Read anything under repos/{id}/{id}/code-quality (3 documented GET endpoints, all plain reads). |
| PATCH | repos/{id}/{id}/code-scanning/ai-scan | write | code scanning | Update AI Scan enablement for a repository. |
| PATCH | repos/{id}/{id}/code-scanning/alerts/{id} | write | code scanning | Update a code scanning alert. |
| POST | repos/{id}/{id}/code-scanning/alerts/{id}/autofix | write | code scanning | Create an autofix for a code scanning alert. |
| POST | repos/{id}/{id}/code-scanning/alerts/{id}/autofix/commits | write | code scanning | Commit an autofix for a code scanning alert. |
| DELETE | repos/{id}/{id}/code-scanning/analyses/{id} | write | code scanning | Delete a code scanning analysis from a repository. |
| DELETE | repos/{id}/{id}/code-scanning/codeql/databases/{id} | write | code scanning | Delete a CodeQL database. |
| POST | repos/{id}/{id}/code-scanning/codeql/variant-analyses | write | code scanning | Create a CodeQL variant analysis. |
| PATCH | repos/{id}/{id}/code-scanning/default-setup | write | code scanning | Update a code scanning default setup configuration. |
| POST | repos/{id}/{id}/code-scanning/sarifs | write | code scanning | Upload an analysis as SARIF data. |
| GET | `repos/{id}/{id}/code-scanning/**` | read | code scanning | Read anything under repos/{id}/{id}/code-scanning (13 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/code-security-configuration | read | code security | Get the code security configuration associated with a repository. |
| GET | repos/{id}/{id}/codeowners/errors | read | repositories | List CODEOWNERS errors. |
| POST | repos/{id}/{id}/codespaces | write | codespaces | Create a codespace in a repository. |
| PUT | repos/{id}/{id}/codespaces/secrets/{id} | write | codespaces | Create or update a repository secret. |
| DELETE | repos/{id}/{id}/codespaces/secrets/{id} | write | codespaces | Delete a repository secret. |
| GET | `repos/{id}/{id}/codespaces/**` | read | codespaces | Read anything under repos/{id}/{id}/codespaces (8 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/collaborators | read | collaborators | List repository collaborators. |
| GET | repos/{id}/{id}/collaborators/{id} | read | collaborators | Check if a user is a repository collaborator. |
| PUT | repos/{id}/{id}/collaborators/{id} | write | collaborators | Add a repository collaborator. |
| DELETE | repos/{id}/{id}/collaborators/{id} | write | collaborators | Remove a repository collaborator. |
| GET | repos/{id}/{id}/collaborators/{id}/permission | read | collaborators | Get repository permissions for a user. |
| GET | repos/{id}/{id}/comments | read | commits | List commit comments for a repository. |
| GET | repos/{id}/{id}/comments/{id} | read | commits | Get a commit comment. |
| PATCH | repos/{id}/{id}/comments/{id} | write | commits | Update a commit comment. |
| DELETE | repos/{id}/{id}/comments/{id} | write | commits | Delete a commit comment. |
| GET | repos/{id}/{id}/comments/{id}/reactions | read | reactions | List reactions for a commit comment. |
| POST | repos/{id}/{id}/comments/{id}/reactions | write | reactions | Create reaction for a commit comment. |
| DELETE | repos/{id}/{id}/comments/{id}/reactions/{id} | write | reactions | Delete a commit comment reaction. |
| POST | repos/{id}/{id}/commits/{id}/comments | write | commits | Create a commit comment. |
| GET | `repos/{id}/{id}/commits/**` | read | commits | Read anything under repos/{id}/{id}/commits (9 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/community/profile | read | metrics | Get community profile metrics. |
| GET | `repos/{id}/{id}/compare/**` | read | commits | Compare two commits. |
| GET | `repos/{id}/{id}/contents/**` | read | repositories | Get repository content. |
| PUT | `repos/{id}/{id}/contents/**` | write | repositories | Create or update file contents. |
| DELETE | `repos/{id}/{id}/contents/**` | write | repositories | Delete a file. |
| GET | repos/{id}/{id}/contributors | read | repositories | List repository contributors. |
| GET | repos/{id}/{id}/copilot/cloud-agent/configuration | read | copilot | Get Copilot cloud agent configuration for a repository. |
| GET | repos/{id}/{id}/copilot/code-review/settings | read | copilot | Get Copilot code review settings for a repository. |
| PATCH | repos/{id}/{id}/copilot/code-review/settings | write | copilot | Update Copilot code review settings for a repository. |
| PATCH | repos/{id}/{id}/dependabot/alerts/{id} | write | dependabot | Update a Dependabot alert. |
| PUT | repos/{id}/{id}/dependabot/runner-settings | write | dependabot | Set repository Dependabot runner settings. |
| PUT | repos/{id}/{id}/dependabot/secrets/{id} | write | dependabot | Create or update a repository secret. |
| DELETE | repos/{id}/{id}/dependabot/secrets/{id} | write | dependabot | Delete a repository secret. |
| GET | `repos/{id}/{id}/dependabot/**` | read | dependabot | Read anything under repos/{id}/{id}/dependabot (6 documented GET endpoints, all plain reads). |
| POST | repos/{id}/{id}/dependency-graph/snapshots | write | dependency graph | Create a snapshot of dependencies for a repository. |
| GET | `repos/{id}/{id}/dependency-graph/**` | read | dependency graph | Read anything under repos/{id}/{id}/dependency-graph (4 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/deployments | read | deployments | List deployments. |
| POST | repos/{id}/{id}/deployments | write | deployments | Create a deployment. |
| GET | repos/{id}/{id}/deployments/{id} | read | deployments | Get a deployment. |
| DELETE | repos/{id}/{id}/deployments/{id} | write | deployments | Delete a deployment. |
| GET | repos/{id}/{id}/deployments/{id}/statuses | read | deployments | List deployment statuses. |
| POST | repos/{id}/{id}/deployments/{id}/statuses | write | deployments | Create a deployment status. |
| GET | repos/{id}/{id}/deployments/{id}/statuses/{id} | read | deployments | Get a deployment status. |
| POST | repos/{id}/{id}/dispatches | write | repositories | Create a repository dispatch event. |
| PUT | repos/{id}/{id}/environments/{id} | write | deployments | Create or update an environment. |
| DELETE | repos/{id}/{id}/environments/{id} | write | deployments | Delete an environment. |
| POST | repos/{id}/{id}/environments/{id}/deployment-branch-policies | write | deployments | Create a deployment branch policy. |
| PUT | repos/{id}/{id}/environments/{id}/deployment-branch-policies/{id} | write | deployments | Update a deployment branch policy. |
| DELETE | repos/{id}/{id}/environments/{id}/deployment-branch-policies/{id} | write | deployments | Delete a deployment branch policy. |
| POST | repos/{id}/{id}/environments/{id}/deployment_protection_rules | write | deployments | Create a custom deployment protection rule on an environment. |
| DELETE | repos/{id}/{id}/environments/{id}/deployment_protection_rules/{id} | write | deployments | Disable a custom protection rule for an environment. |
| PUT | repos/{id}/{id}/environments/{id}/secrets/{id} | write | actions | Create or update an environment secret. |
| DELETE | repos/{id}/{id}/environments/{id}/secrets/{id} | write | actions | Delete an environment secret. |
| POST | repos/{id}/{id}/environments/{id}/variables | write | actions | Create an environment variable. |
| PATCH | repos/{id}/{id}/environments/{id}/variables/{id} | write | actions | Update an environment variable. |
| DELETE | repos/{id}/{id}/environments/{id}/variables/{id} | write | actions | Delete an environment variable. |
| GET | `repos/{id}/{id}/environments/**` | read | deployments | Read anything under repos/{id}/{id}/environments (12 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/events | read | activity | List repository events. |
| GET | repos/{id}/{id}/forks | read | repositories | List forks. |
| POST | repos/{id}/{id}/forks | write | repositories | Create a fork. |
| POST | repos/{id}/{id}/generate | write | repositories | Create a repository using a template. |
| POST | repos/{id}/{id}/git/blobs | write | git database | Create a blob. |
| GET | repos/{id}/{id}/git/blobs/{id} | read | git database | Get a blob. |
| POST | repos/{id}/{id}/git/commits | write | git database | Create a commit. |
| GET | repos/{id}/{id}/git/commits/{id} | read | git database | Get a commit object. |
| GET | `repos/{id}/{id}/git/matching-refs/**` | read | git database | List matching references. |
| GET | `repos/{id}/{id}/git/ref/**` | read | git database | Get a reference. |
| POST | repos/{id}/{id}/git/refs | write | git database | Create a reference. |
| PATCH | `repos/{id}/{id}/git/refs/**` | write | git database | Update a reference. |
| DELETE | `repos/{id}/{id}/git/refs/**` | write | git database | Delete a reference. |
| POST | repos/{id}/{id}/git/tags | write | git database | Create a tag object. |
| GET | repos/{id}/{id}/git/tags/{id} | read | git database | Get a tag. |
| POST | repos/{id}/{id}/git/trees | write | git database | Create a tree. |
| GET | repos/{id}/{id}/git/trees/{id} | read | git database | Get a tree. |
| GET | repos/{id}/{id}/hash-algorithm | read | repositories | Get the hash algorithm for a repository. |
| GET | repos/{id}/{id}/hooks | write | repositories | List repository webhooks; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| POST | repos/{id}/{id}/hooks | write | repositories | Create a repository webhook. |
| GET | repos/{id}/{id}/hooks/{id} | write | repositories | Get a repository webhook; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| PATCH | repos/{id}/{id}/hooks/{id} | write | repositories | Update a repository webhook. |
| DELETE | repos/{id}/{id}/hooks/{id} | write | repositories | Delete a repository webhook. |
| GET | repos/{id}/{id}/hooks/{id}/config | write | repositories | Get a webhook configuration for a repository; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| PATCH | repos/{id}/{id}/hooks/{id}/config | write | repositories | Update a webhook configuration for a repository. |
| GET | repos/{id}/{id}/hooks/{id}/deliveries | write | repositories | List deliveries for a repository webhook; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| GET | repos/{id}/{id}/hooks/{id}/deliveries/{id} | write | repositories | Get a delivery for a repository webhook; kept out of read: returns webhook URLs and delivery headers, which can embed third-party credentials. |
| POST | repos/{id}/{id}/hooks/{id}/deliveries/{id}/attempts | write | repositories | Redeliver a delivery for a repository webhook. |
| POST | repos/{id}/{id}/hooks/{id}/pings | write | repositories | Ping a repository webhook. |
| POST | repos/{id}/{id}/hooks/{id}/tests | write | repositories | Test the push repository webhook. |
| GET | repos/{id}/{id}/immutable-releases | read | repositories | Check if immutable releases are enabled for a repository. |
| PUT | repos/{id}/{id}/immutable-releases | write | repositories | Enable immutable releases. |
| DELETE | repos/{id}/{id}/immutable-releases | write | repositories | Disable immutable releases. |
| GET | repos/{id}/{id}/installation | read | apps | Get a repository installation for the authenticated app. |
| PUT | repos/{id}/{id}/interaction-limits | write | interactions | Set interaction restrictions for a repository. |
| DELETE | repos/{id}/{id}/interaction-limits | write | interactions | Remove interaction restrictions for a repository. |
| PUT | repos/{id}/{id}/interaction-limits/pulls/bypass-list | write | interactions | Add users to the pull request creation cap bypass list for a repository. |
| DELETE | repos/{id}/{id}/interaction-limits/pulls/bypass-list | write | interactions | Remove users from the pull request creation cap bypass list for a repository. |
| PATCH | repos/{id}/{id}/interaction-limits/pulls/creation-cap | write | interactions | Update pull request creation cap for a repository. |
| GET | `repos/{id}/{id}/interaction-limits/**` | read | interactions | Read anything under repos/{id}/{id}/interaction-limits (3 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/invitations | read | collaborators | List repository invitations. |
| PATCH | repos/{id}/{id}/invitations/{id} | write | collaborators | Update a repository invitation. |
| DELETE | repos/{id}/{id}/invitations/{id} | write | collaborators | Delete a repository invitation. |
| GET | repos/{id}/{id}/issue-types | read | repositories | List issue types for a repository. |
| GET | repos/{id}/{id}/issues | read | issues | List repository issues. |
| POST | repos/{id}/{id}/issues | write | issues | Create an issue. |
| GET | repos/{id}/{id}/issues/comments | read | issues | List issue comments for a repository. |
| GET | repos/{id}/{id}/issues/comments/{id} | read | issues | Get an issue comment. |
| PATCH | repos/{id}/{id}/issues/comments/{id} | write | issues | Update an issue comment. |
| DELETE | repos/{id}/{id}/issues/comments/{id} | write | issues | Delete an issue comment. |
| PUT | repos/{id}/{id}/issues/comments/{id}/pin | write | issues | Pin an issue comment. |
| DELETE | repos/{id}/{id}/issues/comments/{id}/pin | write | issues | Unpin an issue comment. |
| GET | repos/{id}/{id}/issues/comments/{id}/reactions | read | reactions | List reactions for an issue comment. |
| POST | repos/{id}/{id}/issues/comments/{id}/reactions | write | reactions | Create reaction for an issue comment. |
| DELETE | repos/{id}/{id}/issues/comments/{id}/reactions/{id} | write | reactions | Delete an issue comment reaction. |
| GET | repos/{id}/{id}/issues/events | read | issues | List issue events for a repository. |
| GET | repos/{id}/{id}/issues/events/{id} | read | issues | Get an issue event. |
| GET | repos/{id}/{id}/issues/{id} | read | issues | Get an issue. |
| PATCH | repos/{id}/{id}/issues/{id} | write | issues | Update an issue. |
| GET | repos/{id}/{id}/issues/{id}/artifacts | read | issues | List issue artifacts. |
| POST | repos/{id}/{id}/issues/{id}/artifacts | write | issues | Create an issue artifact. |
| GET | repos/{id}/{id}/issues/{id}/artifacts/{id} | read | issues | Get an issue artifact. |
| PATCH | repos/{id}/{id}/issues/{id}/artifacts/{id} | write | issues | Update an issue artifact. |
| DELETE | repos/{id}/{id}/issues/{id}/artifacts/{id} | write | issues | Delete an issue artifact. |
| POST | repos/{id}/{id}/issues/{id}/assignees | write | issues | Add assignees to an issue. |
| DELETE | repos/{id}/{id}/issues/{id}/assignees | write | issues | Remove assignees from an issue. |
| GET | repos/{id}/{id}/issues/{id}/assignees/{id} | read | issues | Check if a user can be assigned to a issue. |
| GET | repos/{id}/{id}/issues/{id}/comments | read | issues | List issue comments. |
| POST | repos/{id}/{id}/issues/{id}/comments | write | issues | Create an issue comment. |
| GET | repos/{id}/{id}/issues/{id}/dependencies/blocked_by | read | issues | List dependencies an issue is blocked by. |
| POST | repos/{id}/{id}/issues/{id}/dependencies/blocked_by | write | issues | Add a dependency an issue is blocked by. |
| DELETE | repos/{id}/{id}/issues/{id}/dependencies/blocked_by/{id} | write | issues | Remove dependency an issue is blocked by. |
| GET | repos/{id}/{id}/issues/{id}/dependencies/blocking | read | issues | List dependencies an issue is blocking. |
| GET | repos/{id}/{id}/issues/{id}/events | read | issues | List issue events. |
| GET | repos/{id}/{id}/issues/{id}/issue-field-values | read | issues | List issue field values for an issue. |
| POST | repos/{id}/{id}/issues/{id}/issue-field-values | write | issues | Add issue field values to an issue. |
| PUT | repos/{id}/{id}/issues/{id}/issue-field-values | write | issues | Set issue field values for an issue. |
| DELETE | repos/{id}/{id}/issues/{id}/issue-field-values/{id} | write | issues | Delete an issue field value from an issue. |
| GET | repos/{id}/{id}/issues/{id}/labels | read | issues | List labels for an issue. |
| POST | repos/{id}/{id}/issues/{id}/labels | write | issues | Add labels to an issue. |
| PUT | repos/{id}/{id}/issues/{id}/labels | write | issues | Set labels for an issue. |
| DELETE | repos/{id}/{id}/issues/{id}/labels | write | issues | Remove all labels from an issue. |
| DELETE | repos/{id}/{id}/issues/{id}/labels/{id} | write | issues | Remove a label from an issue. |
| PUT | repos/{id}/{id}/issues/{id}/lock | write | issues | Lock an issue. |
| DELETE | repos/{id}/{id}/issues/{id}/lock | write | issues | Unlock an issue. |
| GET | repos/{id}/{id}/issues/{id}/parent | read | issues | Get parent issue. |
| GET | repos/{id}/{id}/issues/{id}/reactions | read | reactions | List reactions for an issue. |
| POST | repos/{id}/{id}/issues/{id}/reactions | write | reactions | Create reaction for an issue. |
| DELETE | repos/{id}/{id}/issues/{id}/reactions/{id} | write | reactions | Delete an issue reaction. |
| GET | repos/{id}/{id}/issues/{id}/relates_to | read | issues | List issues related to an issue. |
| POST | repos/{id}/{id}/issues/{id}/relates_to | write | issues | Add a related issue. |
| DELETE | repos/{id}/{id}/issues/{id}/relates_to/{id} | write | issues | Remove a related issue. |
| DELETE | repos/{id}/{id}/issues/{id}/sub_issue | write | issues | Remove sub-issue. |
| GET | repos/{id}/{id}/issues/{id}/sub_issues | read | issues | List sub-issues. |
| POST | repos/{id}/{id}/issues/{id}/sub_issues | write | issues | Add sub-issue. |
| PATCH | repos/{id}/{id}/issues/{id}/sub_issues/priority | write | issues | Reprioritize sub-issue. |
| GET | repos/{id}/{id}/issues/{id}/suggestions | read | issues | List issue suggestions. |
| POST | repos/{id}/{id}/issues/{id}/suggestions/{id}/approve | write | issues | Approve an issue suggestion. |
| POST | repos/{id}/{id}/issues/{id}/suggestions/{id}/dismiss | write | issues | Dismiss an issue suggestion. |
| GET | repos/{id}/{id}/issues/{id}/timeline | read | issues | List timeline events for an issue. |
| GET | repos/{id}/{id}/keys | read | deploy keys | List deploy keys. |
| POST | repos/{id}/{id}/keys | write | deploy keys | Create a deploy key. |
| GET | repos/{id}/{id}/keys/{id} | read | deploy keys | Get a deploy key. |
| DELETE | repos/{id}/{id}/keys/{id} | write | deploy keys | Delete a deploy key. |
| GET | repos/{id}/{id}/labels | read | issues | List labels for a repository. |
| POST | repos/{id}/{id}/labels | write | issues | Create a label. |
| GET | repos/{id}/{id}/labels/{id} | read | issues | Get a label. |
| PATCH | repos/{id}/{id}/labels/{id} | write | issues | Update a label. |
| DELETE | repos/{id}/{id}/labels/{id} | write | issues | Delete a label. |
| GET | repos/{id}/{id}/languages | read | repositories | List repository languages. |
| GET | repos/{id}/{id}/license | read | licenses | Get the license for a repository. |
| POST | repos/{id}/{id}/merge-upstream | write | branches | Sync a fork branch with the upstream repository. |
| POST | repos/{id}/{id}/merges | write | branches | Merge a branch. |
| GET | repos/{id}/{id}/milestones | read | issues | List milestones. |
| POST | repos/{id}/{id}/milestones | write | issues | Create a milestone. |
| GET | repos/{id}/{id}/milestones/{id} | read | issues | Get a milestone. |
| PATCH | repos/{id}/{id}/milestones/{id} | write | issues | Update a milestone. |
| DELETE | repos/{id}/{id}/milestones/{id} | write | issues | Delete a milestone. |
| GET | repos/{id}/{id}/milestones/{id}/labels | read | issues | List labels for issues in a milestone. |
| GET | repos/{id}/{id}/notifications | read | activity | List repository notifications for the authenticated user. |
| PUT | repos/{id}/{id}/notifications | write | activity | Mark repository notifications as read. |
| GET | repos/{id}/{id}/pages | read | pages | Get a GitHub Pages site. |
| POST | repos/{id}/{id}/pages | write | pages | Create a GitHub Pages site. |
| PUT | repos/{id}/{id}/pages | write | pages | Update information about a GitHub Pages site. |
| DELETE | repos/{id}/{id}/pages | write | pages | Delete a GitHub Pages site. |
| GET | repos/{id}/{id}/pages/builds | read | pages | List GitHub Pages builds. |
| POST | repos/{id}/{id}/pages/builds | write | pages | Request a GitHub Pages build. |
| GET | repos/{id}/{id}/pages/builds/latest | read | pages | Get latest Pages build. |
| GET | repos/{id}/{id}/pages/builds/{id} | read | pages | Get GitHub Pages build. |
| POST | repos/{id}/{id}/pages/deployments | write | pages | Create a GitHub Pages deployment. |
| GET | repos/{id}/{id}/pages/deployments/{id} | read | pages | Get the status of a GitHub Pages deployment. |
| POST | repos/{id}/{id}/pages/deployments/{id}/cancel | write | pages | Cancel a GitHub Pages deployment. |
| GET | repos/{id}/{id}/pages/health | write | pages | Get a DNS health check for GitHub Pages; kept out of read: queues a Pages DNS health check job on first call. |
| GET | repos/{id}/{id}/planning-statuses | read | repositories | List planning statuses for a repository. |
| GET | repos/{id}/{id}/private-vulnerability-reporting | read | repositories | Check if private vulnerability reporting is enabled for a repository. |
| PUT | repos/{id}/{id}/private-vulnerability-reporting | write | repositories | Enable private vulnerability reporting for a repository. |
| DELETE | repos/{id}/{id}/private-vulnerability-reporting | write | repositories | Disable private vulnerability reporting for a repository. |
| GET | repos/{id}/{id}/properties/values | read | repositories | Get all custom property values for a repository. |
| PATCH | repos/{id}/{id}/properties/values | write | repositories | Create or update custom property values for a repository. |
| GET | repos/{id}/{id}/pulls | read | pull requests | List pull requests. |
| POST | repos/{id}/{id}/pulls | write | pull requests | Create a pull request. |
| GET | repos/{id}/{id}/pulls/comments | read | pull requests | List review comments in a repository. |
| GET | repos/{id}/{id}/pulls/comments/{id} | read | pull requests | Get a review comment for a pull request. |
| PATCH | repos/{id}/{id}/pulls/comments/{id} | write | pull requests | Update a review comment for a pull request. |
| DELETE | repos/{id}/{id}/pulls/comments/{id} | write | pull requests | Delete a review comment for a pull request. |
| GET | repos/{id}/{id}/pulls/comments/{id}/reactions | read | reactions | List reactions for a pull request review comment. |
| POST | repos/{id}/{id}/pulls/comments/{id}/reactions | write | reactions | Create reaction for a pull request review comment. |
| DELETE | repos/{id}/{id}/pulls/comments/{id}/reactions/{id} | write | reactions | Delete a pull request comment reaction. |
| GET | repos/{id}/{id}/pulls/{id} | read | pull requests | Get a pull request. |
| PATCH | repos/{id}/{id}/pulls/{id} | write | pull requests | Update a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/codespaces | write | codespaces | Create a codespace from a pull request. |
| GET | repos/{id}/{id}/pulls/{id}/comments | read | pull requests | List review comments on a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/comments | write | pull requests | Create a review comment for a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/comments/{id}/replies | write | pull requests | Create a reply for a review comment. |
| GET | repos/{id}/{id}/pulls/{id}/commits | read | pull requests | List commits on a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/copilot-code-review | write | pull requests | Request a Copilot code review for a pull request. |
| GET | repos/{id}/{id}/pulls/{id}/files | read | pull requests | List pull requests files. |
| GET | repos/{id}/{id}/pulls/{id}/merge | read | pull requests | Check if a pull request has been merged. |
| PUT | repos/{id}/{id}/pulls/{id}/merge | write | pull requests | Merge a pull request. |
| PUT | repos/{id}/{id}/pulls/{id}/merge-async | write | pull requests | Merge a pull request asynchronously. |
| GET | repos/{id}/{id}/pulls/{id}/merge-async/{id} | read | pull requests | Get the result of an asynchronous merge. |
| GET | repos/{id}/{id}/pulls/{id}/requested_reviewers | read | pull requests | Get all requested reviewers for a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/requested_reviewers | write | pull requests | Request reviewers for a pull request. |
| DELETE | repos/{id}/{id}/pulls/{id}/requested_reviewers | write | pull requests | Remove requested reviewers from a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/requested_reviewers/rerequest | write | pull requests | Rerequest reviewers for a pull request. |
| GET | repos/{id}/{id}/pulls/{id}/reviews | read | pull requests | List reviews for a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/reviews | write | pull requests | Create a review for a pull request. |
| GET | repos/{id}/{id}/pulls/{id}/reviews/{id} | read | pull requests | Get a review for a pull request. |
| PUT | repos/{id}/{id}/pulls/{id}/reviews/{id} | write | pull requests | Update a review for a pull request. |
| DELETE | repos/{id}/{id}/pulls/{id}/reviews/{id} | write | pull requests | Delete a pending review for a pull request. |
| GET | repos/{id}/{id}/pulls/{id}/reviews/{id}/comments | read | pull requests | List comments for a pull request review. |
| PUT | repos/{id}/{id}/pulls/{id}/reviews/{id}/dismissals | write | pull requests | Dismiss a review for a pull request. |
| POST | repos/{id}/{id}/pulls/{id}/reviews/{id}/events | write | pull requests | Submit a review for a pull request. |
| PUT | repos/{id}/{id}/pulls/{id}/update-branch | write | pull requests | Update a pull request branch. |
| GET | repos/{id}/{id}/readme | read | repositories | Get a repository README. |
| GET | `repos/{id}/{id}/readme/**` | read | repositories | Get a repository README for a directory. |
| GET | repos/{id}/{id}/releases | read | releases | List releases. |
| POST | repos/{id}/{id}/releases | write | releases | Create a release. |
| GET | repos/{id}/{id}/releases/assets/{id} | read | releases | Get a release asset. |
| PATCH | repos/{id}/{id}/releases/assets/{id} | write | releases | Update a release asset. |
| DELETE | repos/{id}/{id}/releases/assets/{id} | write | releases | Delete a release asset. |
| POST | repos/{id}/{id}/releases/generate-notes | write | releases | Generate release notes content for a release. |
| GET | repos/{id}/{id}/releases/latest | read | releases | Get the latest release. |
| GET | `repos/{id}/{id}/releases/tags/**` | read | releases | Get a release by tag name. |
| GET | repos/{id}/{id}/releases/{id} | read | releases | Get a release. |
| PATCH | repos/{id}/{id}/releases/{id} | write | releases | Update a release. |
| DELETE | repos/{id}/{id}/releases/{id} | write | releases | Delete a release. |
| GET | repos/{id}/{id}/releases/{id}/assets | read | releases | List release assets. |
| POST | repos/{id}/{id}/releases/{id}/assets | write | releases | Upload a release asset. |
| GET | repos/{id}/{id}/releases/{id}/reactions | read | reactions | List reactions for a release. |
| POST | repos/{id}/{id}/releases/{id}/reactions | write | reactions | Create reaction for a release. |
| DELETE | repos/{id}/{id}/releases/{id}/reactions/{id} | write | reactions | Delete a release reaction. |
| GET | `repos/{id}/{id}/rules/branches/**` | read | repositories | Get rules for a branch. |
| POST | repos/{id}/{id}/rulesets | write | repositories | Create a repository ruleset. |
| PUT | repos/{id}/{id}/rulesets/{id} | write | repositories | Update a repository ruleset. |
| DELETE | repos/{id}/{id}/rulesets/{id} | write | repositories | Delete a repository ruleset. |
| GET | `repos/{id}/{id}/rulesets/**` | read | repositories | Read anything under repos/{id}/{id}/rulesets (6 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/secret-scanning/alerts | write | secret scanning | List secret scanning alerts for a repository; kept out of read: returns the leaked secret values found by secret scanning. |
| GET | repos/{id}/{id}/secret-scanning/alerts/{id} | write | secret scanning | Get a secret scanning alert; kept out of read: returns the leaked secret values found by secret scanning. |
| PATCH | repos/{id}/{id}/secret-scanning/alerts/{id} | write | secret scanning | Update a secret scanning alert. |
| GET | repos/{id}/{id}/secret-scanning/alerts/{id}/locations | write | secret scanning | List locations for a secret scanning alert; kept out of read: returns the leaked secret values found by secret scanning. |
| GET | repos/{id}/{id}/secret-scanning/custom-patterns | read | secret scanning | List repository custom patterns. |
| POST | repos/{id}/{id}/secret-scanning/custom-patterns | write | secret scanning | Bulk create repository custom patterns. |
| DELETE | repos/{id}/{id}/secret-scanning/custom-patterns | write | secret scanning | Bulk delete repository custom patterns. |
| PATCH | repos/{id}/{id}/secret-scanning/custom-patterns/{id} | write | secret scanning | Update a repository custom pattern. |
| POST | repos/{id}/{id}/secret-scanning/push-protection-bypasses | write | secret scanning | Create a push protection bypass. |
| GET | repos/{id}/{id}/secret-scanning/scan-history | read | secret scanning | Get secret scanning scan history for a repository. |
| POST | repos/{id}/{id}/security-advisories | write | security advisories | Create a repository security advisory. |
| POST | repos/{id}/{id}/security-advisories/reports | write | security advisories | Privately report a security vulnerability. |
| PATCH | repos/{id}/{id}/security-advisories/{id} | write | security advisories | Update a repository security advisory. |
| POST | repos/{id}/{id}/security-advisories/{id}/comments | write | security advisories | Create a repository advisory comment. |
| PATCH | repos/{id}/{id}/security-advisories/{id}/comments/{id} | write | security advisories | Update a repository advisory comment. |
| POST | repos/{id}/{id}/security-advisories/{id}/cve | write | security advisories | Request a CVE for a repository security advisory. |
| POST | repos/{id}/{id}/security-advisories/{id}/forks | write | security advisories | Create a temporary private fork. |
| GET | `repos/{id}/{id}/security-advisories/**` | read | security advisories | Read anything under repos/{id}/{id}/security-advisories (4 documented GET endpoints, all plain reads). |
| GET | repos/{id}/{id}/stacks | read | pull requests | List pull request stacks. |
| POST | repos/{id}/{id}/stacks | write | pull requests | Create a pull request stack. |
| GET | repos/{id}/{id}/stacks/{id} | read | pull requests | Get a pull request stack. |
| POST | repos/{id}/{id}/stacks/{id}/add | write | pull requests | Add pull requests to a pull request stack. |
| POST | repos/{id}/{id}/stacks/{id}/unstack | write | pull requests | Remove pull requests from a pull request stack. |
| GET | repos/{id}/{id}/stargazers | read | activity | List stargazers. |
| GET | repos/{id}/{id}/stargazers/count | read | activity | Get stargazer count. |
| GET | repos/{id}/{id}/stargazers/history | read | activity | Get repository star history. |
| GET | `repos/{id}/{id}/stats/**` | read | metrics | Read anything under repos/{id}/{id}/stats (5 documented GET endpoints, all plain reads). |
| POST | repos/{id}/{id}/statuses/{id} | write | commits | Create a commit status. |
| GET | repos/{id}/{id}/subscribers | read | activity | List watchers. |
| GET | repos/{id}/{id}/subscription | read | activity | Get a repository subscription. |
| PUT | repos/{id}/{id}/subscription | write | activity | Set a repository subscription. |
| DELETE | repos/{id}/{id}/subscription | write | activity | Delete a repository subscription. |
| GET | repos/{id}/{id}/tags | read | repositories | List repository tags. |
| GET | `repos/{id}/{id}/tarball/**` | read | repositories | Download a repository archive (tar). |
| GET | repos/{id}/{id}/teams | read | repositories | List repository teams. |
| GET | repos/{id}/{id}/topics | read | repositories | Get all repository topics. |
| PUT | repos/{id}/{id}/topics | write | repositories | Replace all repository topics. |
| GET | `repos/{id}/{id}/traffic/**` | read | metrics | Read anything under repos/{id}/{id}/traffic (4 documented GET endpoints, all plain reads). |
| POST | repos/{id}/{id}/transfer | write | repositories | Transfer a repository. |
| GET | repos/{id}/{id}/vulnerability-alerts | read | repositories | Check if vulnerability alerts are enabled for a repository. |
| PUT | repos/{id}/{id}/vulnerability-alerts | write | repositories | Enable vulnerability alerts. |
| DELETE | repos/{id}/{id}/vulnerability-alerts | write | repositories | Disable vulnerability alerts. |
| GET | `repos/{id}/{id}/zipball/**` | read | repositories | Download a repository archive (zip). |
| GET | repositories | read | repositories | List public repositories. |
| GET | search/code | read | search | Search code. |
| GET | search/commits | read | search | Search commits. |
| GET | search/issues | read | search | Search issues and pull requests. |
| GET | search/labels | read | search | Search labels. |
| GET | search/repositories | read | search | Search repositories. |
| GET | search/topics | read | search | Search topics. |
| GET | search/users | read | search | Search users. |
| PATCH | teams/{id} | write | teams | Update a team (Legacy). |
| DELETE | teams/{id} | write | teams | Delete a team (Legacy). |
| PUT | teams/{id}/members/{id} | write | teams | Add team member (Legacy). |
| DELETE | teams/{id}/members/{id} | write | teams | Remove team member (Legacy). |
| PUT | teams/{id}/memberships/{id} | write | teams | Add or update team membership for a user (Legacy). |
| DELETE | teams/{id}/memberships/{id} | write | teams | Remove team membership for a user (Legacy). |
| PUT | teams/{id}/repos/{id}/{id} | write | teams | Add or update team repository permissions (Legacy). |
| DELETE | teams/{id}/repos/{id}/{id} | write | teams | Remove a repository from a team (Legacy). |
| GET | `teams/**` | read | teams | Read anything under teams (8 documented GET endpoints, all plain reads). |
| GET | user | read | users | Get the authenticated user. |
| PATCH | user | write | users | Update the authenticated user. |
| GET | user/blocks | read | users | List users blocked by the authenticated user. |
| GET | user/blocks/{id} | read | users | Check if a user is blocked by the authenticated user. |
| PUT | user/blocks/{id} | write | users | Block a user. |
| DELETE | user/blocks/{id} | write | users | Unblock a user. |
| POST | user/codespaces | write | codespaces | Create a codespace for the authenticated user. |
| PUT | user/codespaces/secrets/{id} | write | codespaces | Create or update a secret for the authenticated user. |
| DELETE | user/codespaces/secrets/{id} | write | codespaces | Delete a secret for the authenticated user. |
| PUT | user/codespaces/secrets/{id}/repositories | write | codespaces | Set selected repositories for a user secret. |
| PUT | user/codespaces/secrets/{id}/repositories/{id} | write | codespaces | Add a selected repository to a user secret. |
| DELETE | user/codespaces/secrets/{id}/repositories/{id} | write | codespaces | Remove a selected repository from a user secret. |
| PATCH | user/codespaces/{id} | write | codespaces | Update a codespace for the authenticated user. |
| DELETE | user/codespaces/{id} | write | codespaces | Delete a codespace for the authenticated user. |
| POST | user/codespaces/{id}/exports | write | codespaces | Export a codespace for the authenticated user. |
| POST | user/codespaces/{id}/publish | write | codespaces | Create a repository from an unpublished codespace. |
| POST | user/codespaces/{id}/start | write | codespaces | Start a codespace for the authenticated user. |
| POST | user/codespaces/{id}/stop | write | codespaces | Stop a codespace for the authenticated user. |
| GET | `user/codespaces/**` | read | codespaces | Read anything under user/codespaces (8 documented GET endpoints, all plain reads). |
| GET | user/docker/conflicts | read | packages | Get list of conflicting packages during Docker migration for authenticated-user. |
| PATCH | user/email/visibility | write | users | Set primary email visibility for the authenticated user. |
| GET | user/emails | read | users | List email addresses for the authenticated user. |
| POST | user/emails | write | users | Add an email address for the authenticated user. |
| DELETE | user/emails | write | users | Delete an email address for the authenticated user. |
| GET | user/followers | read | users | List followers of the authenticated user. |
| GET | user/following | read | users | List the people the authenticated user follows. |
| GET | user/following/{id} | read | users | Check if a person is followed by the authenticated user. |
| PUT | user/following/{id} | write | users | Follow a user. |
| DELETE | user/following/{id} | write | users | Unfollow a user. |
| GET | user/gpg_keys | read | users | List GPG keys for the authenticated user. |
| POST | user/gpg_keys | write | users | Create a GPG key for the authenticated user. |
| GET | user/gpg_keys/{id} | read | users | Get a GPG key for the authenticated user. |
| DELETE | user/gpg_keys/{id} | write | users | Delete a GPG key for the authenticated user. |
| GET | user/installations | read | apps | List app installations accessible to the user access token. |
| GET | user/installations/{id}/repositories | read | apps | List repositories accessible to the user access token. |
| PUT | user/installations/{id}/repositories/{id} | write | apps | Add a repository to an app installation. |
| DELETE | user/installations/{id}/repositories/{id} | write | apps | Remove a repository from an app installation. |
| GET | user/interaction-limits | read | interactions | Get interaction restrictions for your public repositories. |
| PUT | user/interaction-limits | write | interactions | Set interaction restrictions for your public repositories. |
| DELETE | user/interaction-limits | write | interactions | Remove interaction restrictions from your public repositories. |
| GET | user/issue-fields | read | users | List issue fields. |
| POST | user/issue-fields | write | users | Create an issue field. |
| PATCH | user/issue-fields/{id} | write | users | Update an issue field. |
| DELETE | user/issue-fields/{id} | write | users | Delete an issue field. |
| GET | user/issue-types | read | users | List issue types. |
| POST | user/issue-types | write | users | Create an issue type. |
| PUT | user/issue-types/{id} | write | users | Update an issue type. |
| DELETE | user/issue-types/{id} | write | users | Delete an issue type. |
| GET | user/issues | read | issues | List user account issues assigned to the authenticated user. |
| GET | user/keys | read | users | List public SSH keys for the authenticated user. |
| POST | user/keys | write | users | Create a public SSH key for the authenticated user. |
| GET | user/keys/{id} | read | users | Get a public SSH key for the authenticated user. |
| DELETE | user/keys/{id} | write | users | Delete a public SSH key for the authenticated user. |
| GET | user/marketplace_purchases | read | apps | List subscriptions for the authenticated user. |
| GET | user/marketplace_purchases/stubbed | read | apps | List subscriptions for the authenticated user (stubbed). |
| GET | user/memberships/orgs | read | organizations | List organization memberships for the authenticated user. |
| GET | user/memberships/orgs/{id} | read | organizations | Get an organization membership for the authenticated user. |
| PATCH | user/memberships/orgs/{id} | write | organizations | Update an organization membership for the authenticated user. |
| POST | user/migrations | write | migrations | Start a user migration. |
| DELETE | user/migrations/{id}/archive | write | migrations | Delete a user migration archive. |
| DELETE | user/migrations/{id}/repos/{id}/lock | write | migrations | Unlock a user repository. |
| GET | `user/migrations/**` | read | migrations | Read anything under user/migrations (4 documented GET endpoints, all plain reads). |
| GET | user/orgs | read | organizations | List organizations for the authenticated user. |
| DELETE | user/packages/{id}/{id} | write | packages | Delete a package for the authenticated user. |
| POST | user/packages/{id}/{id}/restore | write | packages | Restore a package for the authenticated user. |
| DELETE | user/packages/{id}/{id}/versions/{id} | write | packages | Delete a package version for the authenticated user. |
| POST | user/packages/{id}/{id}/versions/{id}/restore | write | packages | Restore a package version for the authenticated user. |
| GET | `user/packages/**` | read | packages | Read anything under user/packages (4 documented GET endpoints, all plain reads). |
| GET | user/public_emails | read | users | List public email addresses for the authenticated user. |
| GET | user/repos | read | repositories | List repositories for the authenticated user. |
| POST | user/repos | write | repositories | Create a repository for the authenticated user. |
| GET | user/repository_invitations | read | collaborators | List repository invitations for the authenticated user. |
| PATCH | user/repository_invitations/{id} | write | collaborators | Accept a repository invitation. |
| DELETE | user/repository_invitations/{id} | write | collaborators | Decline a repository invitation. |
| GET | user/social_accounts | read | users | List social accounts for the authenticated user. |
| POST | user/social_accounts | write | users | Add social accounts for the authenticated user. |
| DELETE | user/social_accounts | write | users | Delete social accounts for the authenticated user. |
| GET | user/ssh_signing_keys | read | users | List SSH signing keys for the authenticated user. |
| POST | user/ssh_signing_keys | write | users | Create a SSH signing key for the authenticated user. |
| GET | user/ssh_signing_keys/{id} | read | users | Get an SSH signing key for the authenticated user. |
| DELETE | user/ssh_signing_keys/{id} | write | users | Delete an SSH signing key for the authenticated user. |
| GET | user/starred | read | activity | List repositories starred by the authenticated user. |
| GET | user/starred/{id}/{id} | read | activity | Check if a repository is starred by the authenticated user. |
| PUT | user/starred/{id}/{id} | write | activity | Star a repository for the authenticated user. |
| DELETE | user/starred/{id}/{id} | write | activity | Unstar a repository for the authenticated user. |
| GET | user/subscriptions | read | activity | List repositories watched by the authenticated user. |
| GET | user/teams | read | teams | List teams for the authenticated user. |
| GET | user/{id} | read | users | Get a user using their ID. |
| POST | user/{id}/projectsV2/{id}/drafts | write | projects | Create draft item for user owned project. |
| GET | users | read | users | List users. |
| GET | users/{id} | read | users | Get a user. |
| POST | users/{id}/attestations/bulk-list | read | users | List attestations by bulk subject digests. |
| POST | users/{id}/attestations/delete-request | write | users | Delete attestations in bulk. |
| DELETE | users/{id}/attestations/digest/{id} | write | users | Delete attestations by subject digest. |
| GET | users/{id}/attestations/{id} | read | users | List attestations. |
| DELETE | users/{id}/attestations/{id} | write | users | Delete attestations by ID. |
| POST | users/{id}/copilot-spaces | write | copilot spaces | Create a Copilot Space for a user. |
| PUT | users/{id}/copilot-spaces/{id} | write | copilot spaces | Set a Copilot Space for a user. |
| DELETE | users/{id}/copilot-spaces/{id} | write | copilot spaces | Delete a Copilot Space for a user. |
| POST | users/{id}/copilot-spaces/{id}/collaborators | write | copilot spaces | Add a collaborator to a Copilot Space for a user. |
| PUT | users/{id}/copilot-spaces/{id}/collaborators/{id}/{id} | write | copilot spaces | Set a collaborator role for a Copilot Space for a user. |
| DELETE | users/{id}/copilot-spaces/{id}/collaborators/{id}/{id} | write | copilot spaces | Remove a collaborator from a Copilot Space for a user. |
| POST | users/{id}/copilot-spaces/{id}/resources | write | copilot spaces | Create a resource for a Copilot Space for a user. |
| PUT | users/{id}/copilot-spaces/{id}/resources/{id} | write | copilot spaces | Set a resource for a Copilot Space for a user. |
| DELETE | users/{id}/copilot-spaces/{id}/resources/{id} | write | copilot spaces | Delete a resource from a Copilot Space for a user. |
| GET | `users/{id}/copilot-spaces/**` | read | copilot spaces | Read anything under users/{id}/copilot-spaces (5 documented GET endpoints, all plain reads). |
| GET | users/{id}/docker/conflicts | read | packages | Get list of conflicting packages during Docker migration for user. |
| GET | users/{id}/events | read | activity | List events for the authenticated user. |
| GET | users/{id}/events/orgs/{id} | read | activity | List organization events for the authenticated user. |
| GET | users/{id}/events/public | read | activity | List public events for a user. |
| GET | users/{id}/followers | read | users | List followers of a user. |
| GET | users/{id}/following | read | users | List the people a user follows. |
| GET | users/{id}/following/{id} | read | users | Check if a user follows another user. |
| GET | users/{id}/gists | read | gists | List gists for a user. |
| GET | users/{id}/gpg_keys | read | users | List GPG keys for a user. |
| GET | users/{id}/hovercard | read | users | Get contextual information for a user. |
| GET | users/{id}/installation | read | apps | Get a user installation for the authenticated app. |
| GET | users/{id}/keys | read | users | List public keys for a user. |
| GET | users/{id}/orgs | read | organizations | List organizations for a user. |
| DELETE | users/{id}/packages/{id}/{id} | write | packages | Delete a package for a user. |
| POST | users/{id}/packages/{id}/{id}/restore | write | packages | Restore a package for a user. |
| DELETE | users/{id}/packages/{id}/{id}/versions/{id} | write | packages | Delete package version for a user. |
| POST | users/{id}/packages/{id}/{id}/versions/{id}/restore | write | packages | Restore package version for a user. |
| GET | `users/{id}/packages/**` | read | packages | Read anything under users/{id}/packages (4 documented GET endpoints, all plain reads). |
| POST | users/{id}/projectsV2/{id}/fields | write | projects | Add field to user owned project. |
| POST | users/{id}/projectsV2/{id}/items | write | projects | Add item to user owned project. |
| PATCH | users/{id}/projectsV2/{id}/items/{id} | write | projects | Update project item for user. |
| DELETE | users/{id}/projectsV2/{id}/items/{id} | write | projects | Delete project item for user. |
| POST | users/{id}/projectsV2/{id}/views | write | projects | Create a view for a user-owned project. |
| GET | `users/{id}/projectsV2/**` | read | projects | Read anything under users/{id}/projectsV2 (7 documented GET endpoints, all plain reads). |
| GET | users/{id}/received_events | read | activity | List events received by the authenticated user. |
| GET | users/{id}/received_events/public | read | activity | List public events received by a user. |
| GET | users/{id}/repos | read | repositories | List repositories for a user. |
| GET | `users/{id}/settings/**` | read | billing | Read anything under users/{id}/settings (4 documented GET endpoints, all plain reads). |
| GET | users/{id}/social_accounts | read | users | List social accounts for a user. |
| GET | users/{id}/ssh_signing_keys | read | users | List SSH signing keys for a user. |
| GET | users/{id}/starred | read | activity | List repositories starred by a user. |
| GET | users/{id}/subscriptions | read | activity | List repositories watched by a user. |
| GET | versions | read | meta | Get all API versions. |
| GET | zen | read | meta | Get the Zen of GitHub. |
| POST | graphql (queries only) | read | graphql | Runs a GraphQL query (read-only operations only). |
| POST | graphql (mutations only) | write | graphql | Runs a GraphQL mutation. |
