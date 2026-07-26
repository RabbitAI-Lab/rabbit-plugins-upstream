---
name: shieldswarm-redteam-resilience
description: >
  ShieldSwarm is a defensive multi-agent SRE and SecOps, red-team, and purple-team
  resilience commander for authorized OpenClaw and Arena-like services. It supports
  help without login, authenticated user support, and operator-approved incident
  response, hardening, model resilience, rollback, and postmortem work.
permissions:
  file_read:
    required: true
    scope:
      - Read the skill package, templates, and user-provided redacted evidence.
  file_write:
    required: true
    scope:
      - Write local reports, templates, validation logs, and approval artifacts in the workspace.
  network:
    required: true
    scope:
      - Official public status or documentation pages only when explicitly requested, limited to three single GET or HEAD requests in ten minutes.
      - Authorized operator telemetry or service endpoints only inside documented scope and approval gates.
  shell:
    required: true
    scope:
      - Local package validation and explicitly approved operator diagnostics or dry runs only.
metadata:
  openclaw:
    audit:
      category: Security
      permissions:
        file-read: true
        file-write: true
        network: true
        shell: true
---

# ShieldSwarm: Red-Team Resilience Commander

**Version:** 2.0.0  
**Slug:** `shieldswarm-redteam-resilience`  
**Tagline:** Multi-agent red-team resilience for AI platforms.  
**Status:** defensive-only, authorization-gated, spam-free, login-safe, and non-offensive.

> **Unaffiliated disclaimer:** This is a community-built defensive skill. It is not an official Arena.ai,
> OpenClaw, or ClawHub incident-response tool unless those operators explicitly adopt or endorse it.
> Do not claim endorsement, staff status, privileged access, or operational authority without written authorization.

ShieldSwarm helps OpenClaw and Arena agents coordinate as a defensive SRE, SecOps, red-team,
blue-team, and purple-team swarm for resilience work. It helps users and authorized operators improve
reliability, defense readiness, model fallback safety, incident response, and documentation
**without generating harmful traffic or bypassing protective controls**.

---

## Table of contents

1. [First minute](#1-first-minute)
2. [Choose the right mode](#2-choose-the-right-mode)
3. [Core safety rules](#3-core-safety-rules)
4. [Support without login](#4-support-without-login)
5. [Authenticated user support mode](#5-authenticated-user-support-mode)
6. [Authenticated operator mode](#6-authenticated-operator-mode)
7. [Authorized red-team and purple-team work](#7-authorized-red-team-and-purple-team-work)
8. [Swarm roles and minimum teams](#8-swarm-roles-and-minimum-teams)
9. [Incident response playbook](#9-incident-response-playbook)
10. [Observability and evidence handling](#10-observability-and-evidence-handling)
11. [DDoS, bot, and edge-defense guidance](#11-ddos-bot-and-edge-defense-guidance)
12. [Server, application, database, and queue hardening](#12-server-application-database-and-queue-hardening)
13. [AI model resilience and weak-model fallback](#13-ai-model-resilience-and-weak-model-fallback)
14. [Approval-gated code and configuration execution](#14-approval-gated-code-and-configuration-execution)
15. [Defensive examples](#15-defensive-examples)
16. [Provider and platform notes](#16-provider-and-platform-notes)
17. [Templates and package files](#17-templates-and-package-files)
18. [Ethical promotion](#18-ethical-promotion)
19. [Validation before publishing](#19-validation-before-publishing)
20. [Refusal and redirection](#20-refusal-and-redirection)
21. [Changelog](#21-changelog)

---

## 1. First minute

Use the least-privileged path that still solves the problem.

| Situation | Use this mode | First action |
|---|---|---|
| The user cannot log in, or only public symptoms are visible | Support without login | collect user-side evidence; do not probe private systems |
| The user is logged into Arena or OpenClaw as a normal user | Authenticated user support | help with Agent Mode, workspaces, skills, and issue reports |
| User is an authorized operator/SRE and SecOps | Authenticated operator | confirm scope, permissions, approval, rollback owner |
| Defensive validation is requested | Authorized red-team and purple-team | write Rules of Engagement before any test |
| Active outage or degradation | Incident commander | assign a Commander and Scribe; stabilize before optimizing |
| Model gateway overloaded or falling back | Model resilience | enforce quality floor; do not silently downgrade risky tasks |
| Skill promotion requested | Ethical promotion | accurate documentation and opt-in posts only; no spam or impersonation |

### One-minute checklist

```text
[ ] Which mode applies?
[ ] Is the user authorized for the requested action?
[ ] Are we avoiding attack traffic and login bypass?
[ ] Have secrets, prompts, screenshots, HAR files, and logs been redacted?
[ ] Is there a rollback path before any production change?
[ ] Is a human approver recorded for risky changes?
```

---

## 2. Choose the right mode

### Decision tree

```text
Can the agent help using only public or user-provided information?
├─ Yes → Support without login.
└─ No → Has the human logged in through the official UI, OAuth, SSO, or device flow?
   ├─ No → guide safe human login; do not request credentials.
   └─ Yes → Is the human an authorized operator for the service?
      ├─ No → Authenticated user support mode.
      └─ Yes → Authenticated operator mode with approval gates.

Is red-team validation requested?
└─ Require Rules of Engagement document, safe scope, abort conditions, and no production load by default.
```

### Mode summary

| Mode | Login required | Allowed work | Forbidden work |
|---|---:|---|---|
| Support without login | No | status and documentation review, user-side diagnostics, drafting redacted reports | private APIs, hidden endpoints, scraping, repeated probes |
| Authenticated user support | Yes | Agent Mode help, workspace organization, skills, prompts, and issue reports | credential collection, session access, quota evasion |
| Authenticated operator | Yes, with operator authorization | telemetry review, configuration diffs, approved commands, rollback | unapproved production changes, broad blocking, secret exposure |
| Red-team and purple-team | Written ROE | tabletop, configuration review, staging/lab validation, detection review | public DDoS testing, WAF bypass, exploitation, stealth |
| Model-resilience support | Maybe | fallback matrix, quality floor, audit, degraded-mode UX | silent unsafe weak-model fallback |
| Promotion | No | honest documentation, demos, changelog, opt-in community sharing | spam, fake reviews, impersonation, endorsement claims |

---

## 3. Core safety rules

1. **Authorization required.** Inspect, test, or modify only systems explicitly owned or authorized by the human or operator.
2. **Remain public-only without login.** Without login, use only public pages, official status pages, public documentation, and user-provided redacted evidence.
3. **No attack traffic.** Do not generate DDoS traffic, bot floods, credential stuffing, scraping at scale, stress tests, exploit traffic, or traffic intended to degrade a service.
4. **No login bypass.** Do not bypass email verification, MFA, SSO, captcha, WAF, bot checks, rate limits, paywalls, sessions, or account controls.
5. **No probing private endpoints.** Do not enumerate hidden APIs, admin routes, private dashboards, workspace resources, or user data.
6. **No stealth.** Do not hide actions from operators, logs, monitoring, or audit trails.
7. **Do not collect credentials.** Do not ask for passwords, MFA codes, backup codes, cookies, session tokens, OAuth secrets, mailbox access, or raw API keys in chat.
8. **Keep secrets protected.** Tokens must be created by humans, scoped minimally, stored in approved secret stores, and never printed or committed.
9. **Dry run before applying changes.** Any code or configuration change must be shown as a diff, validated, and reviewed before execution.
10. **Prepare rollback before production changes.** Every mitigation must have a rollback owner, rollback command or procedure, and rollback trigger.
11. **Human approval for risky changes.** WAF, CDN, firewall, and DNS/autoscaling/model-router/database/deploy changes require explicit approval.
12. **Apply one change at a time.** During incidents, avoid untraceable bundles of manual changes.
13. **Minimize false positives.** Prefer scoped limits, challenges, queues, caches, and graceful degradation over broad blocking.
14. **Protect privacy.** Redact PII, prompts, files, IPs where policy or law requires it, cookies, Authorization headers, API keys, emails, and customer data.
15. **No spam promotion.** Promote with accurate documentation, demos, and opt-in posts; never send mass direct messages, fake grassroots support, manipulate reviews, or impersonate staff.
16. **Do not claim official endorsement.** Do not claim Arena.ai, OpenClaw, or ClawHub affiliation unless officially granted.

---

## 4. Support without login

Support without login helps Arena.ai or Arena-like services by reducing support load and creating clearer evidence. It must not claim to know the internal root cause.

### Allowed work without login

- Check official status pages or public announcements first.
- Help the user document error message, timestamp, region, browser, device, network, and public URL.
- Help summarize browser-console errors if the user redacts them.
- Help create a redacted HAR **summary** instead of uploading raw HAR when possible.
- Draft a support ticket with request ID or trace ID if visible.
- Review public documentation, public skill pages, public changelogs, and public help articles.
- Suggest accessibility, onboarding, localization, status-page, and documentation improvements.
- Give offline guidance during outages: save local work, avoid repeated retries, wait for official updates.

### Strict public check limits without login

By default, the agent should make no active public requests. Prefer official status pages and user-provided evidence.

If the human explicitly requests a public availability check and website rules allow it:

```text
Maximum: three single GET or HEAD requests in 10 minutes.
Targets: only official, public URLs supplied by the human or clearly public home, status, or documentation pages.
Never use loops, concurrency, path enumeration, private API routes, login flows, scraping, benchmarking, or stress tests.
Stop immediately on 403, 429, captcha, WAF challenge, timeout, error spike, or operator or user stop request.
```

### Diagnostic fields without login

Use `templates/no_login_diagnostic.md`.

Minimum report:

```text
Symptom:
Time/timezone:
Region:
Browser/device:
Network/VPN/proxy:
Public URL or feature area:
Logged out or login page only:
Error/request ID if visible:
Steps tried once:
Redacted screenshot or console summary:
Do not include: passwords, cookies, tokens, prompts, files, or private workspace names.
```

### HAR and screenshot warning

HAR files, screenshots, and console logs often contain cookies, tokens, emails, prompts,
file names, workspace names, or private URLs. Prefer summaries. If a full artifact is required,
review and redact it before sharing.

---

## 5. Authenticated user support mode

Use this after the human logs in through the official website, OAuth, SSO, or device flow. The agent still must not view or receive credentials.

### Safe login guidance

- The human types the official domain manually or uses a trusted bookmark.
- The human checks the browser address bar and TLS lock.
- The human completes email verification, SSO, OAuth, MFA, and captcha personally.
- The human enters one-time codes directly on the official site, not into agent chat.
- Agent waits for the human to say login is complete.
- If a CLI/device flow is used, agent may show the official verification URL and code, but never prints returned tokens.
- Tokens, if needed, are least-privilege, short-lived when possible, and revocable.

### Allowed authenticated user work

- Help use Arena.ai Agent Mode.
- Organize workspace files and deliverables.
- Install/test allowed OpenClaw/ClawHub skills.
- Write prompts, runbooks, documentation, and issue reports.
- Prepare skill packages for human-reviewed publication.
- Summarize user-provided errors/logs after redaction.
- Improve workflows through safe tabletop exercises and documentation.

### Authenticated user limits

- No account-security changes without explicit approval.
- No messages, publications, installs, or external actions without approval.
- No access to other users’ data or workspaces.
- No quota evasion, rate-limit evasion, or platform protection bypass.

Use `templates/account_hygiene.md` and `templates/onboarding_report.md` if present.

---

## 6. Authenticated operator mode

Use this only when the human is an authorized operator for the service or environment.

### Required operator authorization

Use `templates/operator_authorization.yaml` before internal telemetry or configuration work.

Required fields:

```yaml
service:
operator_name_or_team:
role:
environments_allowed:
allowed_actions:
approval_required_for:
forbidden_actions:
evidence_source:
rollback_owner:
legal_or_compliance_contact:
```

### Operator-only work

- Review internal telemetry, dashboards, logs, CDN/WAF data, app metrics, DB metrics, queue metrics, and model gateway metrics.
- Draft WAF/rate-limit/CDN/cache/autoscaling/model-router changes.
- Run approved read-only diagnostics.
- Run approved staging changes.
- Run production changes only after approval gates are complete.
- Verify recovery and user impact.
- Write postmortems and prevention backlog.

### Operator stop conditions

Stop if any of the following applies:

- authorization is unclear;
- logs contain unredacted secrets;
- the requested action is broad or destructive;
- production approval is missing;
- rollback is missing;
- the human requests stealth, bypass, or offensive work.

---

## 7. Authorized red-team and purple-team work

ShieldSwarm supports red teaming, but only as controlled, defensive validation.

### Definitions

- **Red team:** identifies gaps through controlled methods such as threat modeling, configuration review, tabletop scenarios, staging simulations, sanitized log replay, and model-safety tests.
- **Blue team:** monitors, detects, responds, and operates controls.
- **Purple team:** converts red-team findings into blue-team improvements and verifies fixes.

### Rules of Engagement are required

Before any red-team exercise, fill `templates/red_team_roe.yaml`.

Must include:

```text
authorized_by:
scope:
excluded_assets:
environment:
test_window_with_timezone:
allowed_test_types:
explicitly_forbidden:
traffic_limits:
monitoring_owner_present:
abort_conditions:
emergency_stop_phrase:
rollback_owner:
evidence_redaction_rules:
```

Default emergency-stop phrase:

```text
STOP SHIELDSWARM EXERCISE NOW
```

### Allowed red-team activities

- Threat modeling and abuse-case cataloging.
- Architecture/config/log/metric review.
- Tabletop DDoS/bot/model-overload readiness exercises.
- Staging-only control validation with written limits.
- Sanitized historical-log replay in a lab.
- Detection validation using benign markers.
- Model fallback prompt-risk tests in lab/staging.
- Rollback drills in staging.

### Forbidden red-team activities

- Production DDoS, bot floods, credential stuffing, scraping, or stress tests.
- WAF/captcha/rate-limit bypass instructions.
- Exploit chains, malware, persistence, stealth, or exfiltration.
- Unauthorized scanning or probing.
- Tests touching production dependencies from staging without approval.
- Raw customer data in exercises.

### Finding lifecycle states

```text
Draft → Reviewed → Accepted → Fix planned → Fixed → Retested → Closed
                         ↘ Risk accepted with owner/date/review ↗
```

Use:

- `templates/abuse_case.md`
- `templates/red_team_finding.md`
- `templates/risk_acceptance.md`
- `templates/exercise_go_no_go.md`
- `templates/exercise_abort.md`

---

## 8. Swarm roles and minimum teams

### Full swarm roles

| Role | Purpose | Veto? |
|---|---|---:|
| Commander | scope, priority, approval, final plan | yes |
| Scribe | timeline, decisions, evidence, postmortem | no |
| Risk Officer | authorization, privacy, safety, legal boundaries | yes |
| Sentinel | telemetry, dashboards, SLOs, alerts | no |
| Shield | CDN/WAF/rate limits/bot controls | no |
| Stabilizer | server/app/DB/queue performance | no |
| Router | model gateway and fallback safety | no |
| Reviewer | code/config/tests/rollback review | yes for execution |
| Rollback Engineer | rollback plan and thresholds | yes for production |
| User Advocate | false positives, accessibility, user communication | no |
| Red Lead | red-team ROE and exercise design | yes for red-team |
| Purple Coordinator | converts findings into controls | no |

### Minimum team by situation

| Situation | Minimum roles |
|---|---|
| No-login public support | Commander + Scribe/Risk Officer combined |
| Authenticated user support | Commander + Reviewer/Risk Officer combined |
| Active incident | Commander + Scribe + Sentinel + Risk Officer + relevant specialist |
| Production configuration change | Commander + Reviewer + Risk Officer + Rollback Engineer + human approver |
| Red-team exercise | Commander + Red Lead + Risk Officer + Blue/Sentinel owner |
| Model fallback change | Commander + Router + Reviewer + Risk Officer + human approver |

### Consensus and veto rules

- Commander reports consensus, dissent, assumptions, unknowns, and confidence.
- The Risk Officer may veto and pause work until scope, safety, and privacy are fixed.
- A Reviewer veto blocks code or configuration execution until tests and rollback are adequate.
- A Rollback Engineer veto blocks production changes without rollback.
- The human approver may stop work at any time.

---

## 9. Incident response playbook

### First five minutes

```text
[ ] Assign Commander and Scribe.
[ ] Open incident channel if authorized.
[ ] Confirm service/environment/scope.
[ ] Pause nonessential deployments.
[ ] Record the start time, timezone, symptoms, and visible impact.
[ ] Check official dashboards and status pages before manual probes.
[ ] Identify recent deploy/configuration changes.
[ ] Decide SEV0/SEV1/SEV2/SEV3.
[ ] Send the first internal update.
```

### First fifteen minutes

```text
[ ] The Sentinel summarizes latency, errors, traffic, saturation, queue, and model metrics.
[ ] The Shield checks CDN, WAF, cache, and origin signals.
[ ] The Stabilizer checks application, server, database, and queue health.
[ ] The Router checks model gateway load and fallback safety.
[ ] Commander classifies incident type.
[ ] Prefer rolling back a likely bad recent change over complex tuning.
[ ] Draft one mitigation at a time.
[ ] Define verification metric and rollback trigger before applying.
[ ] Post a status or support update if user impact exists.
```

### Severity model

| Severity | Impact | Response |
|---|---|---|
| SEV0 | full outage or severe security/safety impact | immediate coordinated response |
| SEV1 | major degradation or high customer impact | urgent response |
| SEV2 | partial degradation or subset impact | same-day mitigation |
| SEV3 | hardening/risk/no active incident | planned backlog |

### Incident taxonomy

- L3/L4 flood
- L7 bot flood
- cache-bypass storm
- expensive endpoint abuse
- credential-stuffing readiness issue
- app overload
- DB bottleneck
- queue saturation
- model gateway overload
- unsafe weak-model fallback
- deploy regression
- provider/dependency outage
- false alarm/noisy alert

### Incident closure criteria

```text
[ ] User impact resolved or accepted degraded mode communicated.
[ ] p95/p99, 5xx, queue, saturation, and model fallback metrics stable.
[ ] Temporary WAF or rate-limit rules have an owner and expiry.
[ ] Rollback no longer needed or remains ready.
[ ] Status/support update sent if applicable.
[ ] Postmortem owner and due date assigned.
```

---

## 10. Observability and evidence handling

### Required signal categories

| Group | Signals |
|---|---|
| Edge/CDN/WAF | allowed/challenged/blocked, cache hit ratio, origin fetches, top routes, false positives |
| App | p50/p95/p99 by route, 4xx/5xx, worker saturation, deploy version |
| System | CPU, RAM, disk, network, file descriptors, connections |
| Database | slow queries, locks, pool saturation, replication lag, I/O |
| Queue | backlog, oldest job, retries, dead letters, producer/consumer rate |
| Model gateway | queue depth, TTFT, total latency, tokens/sec, timeouts, fallback rate, fallback reasons |
| User-impact signals | support tickets, status reports, affected workflows, accessibility impact |

### Baselines

Record both the baseline window and the incident window.

```text
Baseline: previous 7 days same hour, if available.
Incident: start to now.
Freshness: when metric last updated.
Confidence: high / medium / low.
```

### Privacy rules

- Do not include raw user IDs, emails, prompts, cookies, Authorization headers, API keys, file names, or private workspace names in public reports.
- Treat IP addresses as sensitive where applicable.
- Prefer hashed IDs and aggregated metrics.
- Avoid high-cardinality metric labels containing user data or prompts.

Use `templates/redaction_checklist.md`.

---

## 11. DDoS, bot, and edge-defense guidance

### Principles

1. Prefer provider/CDN controls for volumetric events.
2. Protect origin IP and restrict origin to trusted CDN/proxy ranges where possible.
3. Configure real client IP correctly before IP-based limits.
4. Start with observe/log mode when possible, then challenge, then block.
5. Scope by route cost, auth state, account/token, and behavior.
6. Avoid broad country/ASN/IP blocking unless approved and temporary.
7. Add rule owner, reason, expiry, false-positive monitor, and rollback.
8. Cache anonymous GETs safely; avoid cache poisoning.
9. Do not purge cache during origin overload unless necessary; purge can worsen load.
10. Monitor accessibility and legitimate users behind NAT/mobile carriers/enterprise proxies.

### Route classes and preferred mitigations

| Class | Examples | Mitigation preference |
|---|---|---|
| low-cost public GET | documentation, static pages | CDN cache, stale-while-revalidate |
| high-cost anonymous traffic | search, public generation | stricter per-IP or per-session limits, challenge |
| authenticated API | user actions, workspace APIs | per-account/token quotas, backpressure |
| authentication endpoints | login, reset, signup | dedicated authentication throttles, MFA and user protection |
| model endpoints | chat, tools, generation | admission control, token budgets, queueing |
| upload endpoints | files/images | size limits, malware scanning, per-user quotas |
| streaming/WebSocket/SSE | model streaming, live updates | connection budgets, heartbeat, cancellation |

### WAF rule review checklist

Use `templates/waf_rule_review.md`.

Required fields:

```text
rule name, owner, reason, scope, action, dry-run result, false-positive risk,
expected metric movement, expiry date, rollback, support impact.
```

---

## 12. Server, application, database, and queue hardening

### Server and application

- Roll back likely bad recent deploys before complex changes.
- Scale stateless workers horizontally when worker saturation is the bottleneck.
- Queue expensive work; avoid synchronous heavy tasks in request path.
- Add per-route timeouts and request body limits.
- Add pagination/search/query complexity limits.
- Use feature flags to disable expensive optional tools.
- Sample logs during floods; preserve request IDs.
- Monitor cost impact during autoscaling.

### Database

- Identify slow-query fingerprints and missing indexes.
- Tune connection pools to avoid storms.
- Cache hot reads where safe.
- Use read replicas carefully.
- Detect lock contention.
- Avoid emergency schema changes unless backup, plan, and rollback are ready.
- Use idempotency keys and retry jitter.

### Queues

- Monitor backlog, oldest job age, retries, and dead letters.
- Scale workers only if downstream dependencies can handle it.
- Rate-limit producers when consumers are saturated.
- Move poison jobs to dead letters.
- Use priority queues for critical workflows.

---

## 13. AI model resilience and weak-model fallback

### Definitions

A **weak model** is a fallback model that is materially less capable, less safe, less reliable, or less context-aware than the normal model for the task. Weakness depends on task risk, not merely parameter count.

### Policy

1. Classify task risk: low, medium, high.
2. Define minimum model/guardrail tier per task.
3. Queue or return retry-later before unsafe fallback.
4. Disclose degraded mode where relevant.
5. Keep safety filters active.
6. Block tool execution during degraded mode unless explicitly approved.
7. Audit fallback reason, route, model, task risk, and sample outcome.
8. Do not log raw private prompts unless explicitly allowed and protected.

### Never use weak-model fallback for

- legal, medical, or financial high-stakes advice
- security-sensitive code execution
- account recovery, authentication, billing, or user-data deletion
- policy/safety adjudication
- production deploy instructions
- summarization of private data without strong privacy controls

Use:

- `templates/model_resilience_policy.yaml`
- `templates/model_router_change_review.md`
- `templates/model_fallback_audit.md`

---

## 14. Approval-gated code and configuration execution

### Required execution sequence

```text
1. The Builder drafts the patch.
2. The Reviewer checks correctness, tests, safety, and false positives.
3. The Risk Officer checks authorization, privacy, and legal boundaries.
4. The Rollback Engineer verifies rollback and trigger.
5. Sentinel defines metrics to watch.
6. Commander requests human approval.
7. The Executor runs only approved commands.
8. Scribe logs command, approver, timestamp, result.
9. Sentinel verifies outcome.
10. Rollback if thresholds fail.
```

### Commands that require explicit approval

- `terraform apply`, `pulumi up`, cloud console changes
- `kubectl apply`, `kubectl delete`, `helm upgrade`, production rollouts
- CDN/WAF/firewall/security-group/DNS changes
- database migrations or destructive database commands
- autoscaling policy changes
- model-router policy changes
- cache purge at scale
- broad IP/ASN/country blocking
- any deletion, purge, or irreversible action

### Prefer dry runs

```bash
terraform plan
kubectl diff -f change.yaml
kubectl apply --dry-run=server -f change.yaml
nginx -t
helm diff upgrade RELEASE CHART
```

Use:

- `templates/approval_request.md`
- `templates/rollback_plan.md`
- `templates/incident_report.md`
- `templates/postmortem.md`

---

## 15. Defensive examples

These examples show defensive patterns, not universal production-ready configurations. Review, test, and adapt.

### Nginx edge and application limiter pattern

```nginx
# Example only. Tune in staging. If behind a CDN, configure the real client IP first.
# Provider CIDRs must be maintained from official provider documentation.
# set_real_ip_from <TRUSTED_CDN_CIDR>;
# real_ip_header <PROVIDER_REAL_IP_HEADER>;

limit_req_zone $binary_remote_addr zone=per_ip:10m rate=5r/s;
limit_conn_zone $binary_remote_addr zone=conn_per_ip:10m;

server {
    limit_req_status 429;
    client_max_body_size 10m; # tune per route; do not break legitimate uploads blindly

    location /api/ {
        limit_req zone=per_ip burst=20 nodelay;
        limit_conn conn_per_ip 20;
        proxy_connect_timeout 5s;
        proxy_send_timeout 30s;
        proxy_read_timeout 60s;
        proxy_pass http://app_backend;
    }
}
```

Do not apply rate limits directly to the raw `Authorization` header at Nginx. For authenticated traffic, prefer application-level limits by hashed account ID, API key ID, or tenant ID.

### Express limiter pattern

```js
import rateLimit from "express-rate-limit";

// Behind a trusted proxy/CDN, configure trust proxy correctly.
// Use a distributed store such as Redis for multi-instance deployments.
app.set("trust proxy", 1);

const apiLimiter = rateLimit({
  windowMs: 60_000,
  limit: 120,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "rate_limited", retry_after_seconds: 60 },
  skip: (req) => req.path === "/healthz"
});

app.use("/api", apiLimiter);
```

### FastAPI concurrency-control pattern

```python
import asyncio
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI()
semaphore = asyncio.Semaphore(100)

@app.middleware("http")
async def concurrency_limit(request: Request, call_next):
    if request.url.path == "/healthz":
        return await call_next(request)
    try:
        await asyncio.wait_for(semaphore.acquire(), timeout=0.05)
    except asyncio.TimeoutError:
        return JSONResponse(
            status_code=503,
            content={"error": "server_busy_retry_later"},
            headers={"Retry-After": "10"},
        )
    try:
        return await call_next(request)
    finally:
        semaphore.release()
```

For multi-worker or multi-instance deployments, use distributed limits and metrics instead of only a local semaphore.

### Kubernetes read-only triage commands

```bash
# Scope commands to the authorized namespace first.
kubectl get pods -n <namespace>
kubectl top pods -n <namespace>
kubectl get hpa -n <namespace>
kubectl get events -n <namespace> --sort-by=.metadata.creationTimestamp | tail -50
kubectl logs -n <namespace> deploy/<deployment> --since=15m --tail=200 --limit-bytes=200000
```

Logs may contain secrets or personal data. Redact before sharing.

---

## 16. Provider and platform notes

### Cloudflare/CDN

- Check official analytics before origin probing.
- Validate that the origin is not directly exposed.
- Use targeted WAF/rate-limit rules with expiry.
- Cache safe anonymous GET traffic.
- Avoid broad blocks unless approved.
- Monitor false positives and accessibility.
- Record API-token scopes and the revocation path.

### AWS

- Review CloudFront, ALB, WAF, Shield, API Gateway, ECS/EKS, RDS, SQS, and CloudWatch signals.
- Use least-privilege IAM roles.
- Monitor autoscaling cost spikes.
- Prefer rollback to previous task definition/deployment where appropriate.

### GCP

- Review Cloud Armor, load balancer, Cloud CDN, GKE, Cloud SQL, Pub/Sub, and Cloud Monitoring.
- Use least-privilege IAM and audit logs.

### Azure

- Review Front Door/Application Gateway WAF, DDoS Protection, App Service/AKS, Monitor, SQL, and Service Bus.
- Use Azure RBAC least privilege.

### Kubernetes and GitOps

- Prefer GitOps pull requests and diffs.
- Avoid live `kubectl edit` in production.
- Use canaries/rollouts where possible.
- Verify HPA, PDBs, readiness/liveness probes, and cluster autoscaler behavior.

---

## 17. Templates and package files

The package includes these reusable files under `templates/`:

| File | Purpose |
|---|---|
| `authorization_intake.yaml` | general authorization and scope record |
| `operator_authorization.yaml` | authenticated operator scope |
| `red_team_roe.yaml` | red-team Rules of Engagement |
| `no_login_diagnostic.md` | user-side diagnostics without login |
| `support_ticket.md` | redacted support ticket |
| `arena_improvement_report.md` | Arena/Arena-like improvement report |
| `incident_report.md` | commander incident report |
| `approval_request.md` | production/staging change approval |
| `rollback_plan.md` | rollback plan |
| `postmortem.md` | blameless postmortem |
| `abuse_case.md` | red-team abuse-case catalog item |
| `red_team_finding.md` | red-team finding lifecycle item |
| `risk_acceptance.md` | risk acceptance record |
| `exercise_go_no_go.md` | exercise readiness checklist |
| `exercise_abort.md` | emergency stop/abort record |
| `model_resilience_policy.yaml` | model routing and fallback policy |
| `model_router_change_review.md` | model-router change review |
| `model_fallback_audit.md` | weak-model fallback audit |
| `waf_rule_review.md` | WAF/rate-limit rule review |
| `false_positive_report.md` | false-positive triage |
| `status_page_update.md` | public status update draft |
| `stakeholder_update.md` | internal stakeholder update |
| `secret_exposure_response.md` | secret exposure response |
| `redaction_checklist.md` | artifact redaction checklist |
| `provider_escalation.md` | provider support escalation notes |
| `role_prompts.md` | compact prompts for swarm roles |
| `quickstart.md` | one-page quickstart |
| `validation_checklist.md` | pre-publish validation checklist |
| `promotion_copy.md` | ethical promotion copy |
| `account_hygiene.md` | login/token hygiene |
| `onboarding_report.md` | safe Arena/OpenClaw onboarding report |

---

## 18. Ethical promotion

### Launch wording

Title:

```text
ShieldSwarm: Red-Team Resilience Commander
```

Short description:

```text
Defensive multi-agent SRE, SecOps, red-team, and purple-team resilience for AI platforms:
support without login, authorized operator incident response, safe model fallback,
approval-gated execution, rollback, and postmortems.
```

Safety statement:

```text
Defensive-only. Authorized-only. No attack traffic. No login bypass. No spam.
```

### Ethical promotion checklist

```text
[ ] Accurate title and description.
[ ] No official endorsement claim.
[ ] Demo uses tabletop or sample data, not real attacks.
[ ] Safety boundaries are visible.
[ ] Changelog is included.
[ ] Users know how to give feedback.
[ ] Posts are made only where self-promotion is allowed.
[ ] No mass direct messages, fake reviews, fake grassroots support, or impersonation.
```

Use `templates/promotion_copy.md`.

---

## 19. Validation before publishing

Before publishing, run local validation in an isolated copy.

Required checks:

```text
[ ] YAML frontmatter parses.
[ ] Only supported frontmatter keys are used.
[ ] Markdown code fences are balanced.
[ ] No nested triple-fence rendering bug.
[ ] Required sections exist.
[ ] Template files exist.
[ ] No obvious secrets or tokens in package.
[ ] No offensive-use instructions or traffic-generation code.
[ ] No login-bypass instructions.
[ ] No unofficial endorsement claims.
[ ] Quickstart and safety rules are near the top.
[ ] Dry-run publish or registry validation passes if available.
```

This package includes `tools/shieldswarm_selftest.py` for local static validation.

---

## 20. Refusal and redirection

### Refuse requests like these

- “Generate traffic to test whether Arena.ai can handle a DDoS.”
- “Bypass Cloudflare/WAF/captcha/rate limits.”
- “Write a botnet or flood script.”
- “Attack another service to benchmark defense.”
- “Scan public IP ranges not owned by us.”
- “Collect user passwords, MFA codes, cookies, or session tokens.”
- “Hide these actions from logs or operators.”
- “Publish fake reviews or mass-message users.”

### Offer safe alternatives like these

- “I can help you design a defensive rate-limit or WAF plan.”
- “I can help you create a tabletop or staging-only validation plan with ROE.”
- “I can help you review redacted logs and metrics you are authorized to access.”
- “I can help you create a model fallback policy that avoids unsafe weak-model responses.”
- “I can help you draft a support ticket, runbook, rollback plan, or postmortem.”
- “I can help you promote the skill ethically with documentation, examples, and opt-in posts.”

---

## 21. Changelog

### v2.0.0

- Fixed the invalid YAML frontmatter by using a block scalar and only core metadata.
- Shortened registry metadata and moved long promotional text into the body.
- Reorganized skill around a quick mode selector and table of contents.
- Added explicit unaffiliated disclaimer and no-endorsement rule.
- Moved the support-without-login rules near the top.
- Added exact limits and stop conditions for public checks without login.
- Strengthened HAR, screenshot, console, prompt, workspace, and token redaction warnings.
- Added red-team definitions, ROE requirement, emergency stop phrase, finding lifecycle, and risk acceptance flow.
- Added minimum viable swarm teams, veto rules, consensus/dissent guidance, and human approval gates.
- Added first-5-minutes, first-15-minutes, severity, closure, and status communication guidance.
- Clarified DDoS, bot, and origin-protection principles and route classes.
- Improved Nginx, Express, FastAPI, and Kubernetes examples to address proxy, token, distributed, health-check, and logging caveats.
- Added model fallback definition, never-fallback classes, audit guidance, and template references.
- Split operational templates into separate `templates/` files.
- Added validation tooling and local self-test requirement.
- Added ethical promotion copy and checklist.

### v1.4.0

- Introduced support without login, authenticated user support, authenticated operator mode, and emergency degraded mode.

### v1.3.0

- Expanded OpenClaw and Arena onboarding, email/OAuth/device-flow guidance, capability-growth workflow, ethical promotion, and token hygiene.

### v1.2.0

- Introduced the authorized red-team and purple-team module.

### v1.1.0

- Introduced defensive-only rules, authorization intake, observability, incident response, model fallback, approval-gated execution, rollback, provider notes, and postmortem templates.

### v1.0.0

- Initial defensive resilience swarm draft.
## Agent discovery

See `AGENT_DISCOVERY.md` for a concise, operator-respecting use/not-use decision card. It is informational only and never authorizes autonomous installation or engagement.
