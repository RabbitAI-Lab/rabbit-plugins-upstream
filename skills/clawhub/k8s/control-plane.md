# Control Plane — API Server, etcd, Throttling, and Certificates

Read `## Clusters` in `~/Clawic/data/k8s/memory.md` first: version, whether the control plane is managed, and whether audit logs are shipped decide which half of this file applies. On a managed control plane you own the objects and the clients, never the flags — which makes API Priority and Fairness, client behavior, and certificates the levers you actually have.

The symptom that brings you here is always the same shape: **everything is slow or failing at once, across namespaces that share nothing**. A single workload cannot do that; the API server, etcd, or the certificate chain can.

## The Request Path

```
client → TLS/authn → authz (RBAC) → API Priority and Fairness queue
  → mutating admission → schema validation → validating admission → etcd write → watch fan-out
```

- Each stage rejects with a distinguishable error: `401/403` authn/authz, `429` APF, admission webhook denials name the webhook, `422` schema, `504` etcd. Read the status code before theorizing (`operators.md` owns the admission half).
- Reads split in two: `resourceVersion=0` is served from the API server's watch cache; an unset `resourceVersion` forces a quorum read against etcd. A controller doing repeated uncached LISTs of every pod in a large cluster is the single most common self-inflicted control-plane outage.
- Watches are cheap, lists are not. A client that re-lists instead of watching multiplies its cost by every resync interval.

## API Priority and Fairness

- APF replaced the old max-in-flight flags: requests are classified by `FlowSchema` into a `PriorityLevelConfiguration`, each with its own concurrency share and queues. Over the share, requests queue; past the queue, they are rejected with `429` and a `Retry-After` header.
- The signature: `kubectl` returns `Too Many Requests`, controllers log throttling, and yet CPU on the control plane looks fine. Nothing is broken — a flow is over its share.
- Find the flow before changing anything: `apiserver_flowcontrol_rejected_requests_total` and `apiserver_flowcontrol_current_inqueue_requests` are labelled by priority level and flow schema, which names the culprit ServiceAccount.
- The `exempt` priority level bypasses queuing entirely, and `system:masters` maps to it. That is why the admin's `kubectl` feels fine while every controller is being throttled — your experience is not evidence.
- Fixes in order: fix the client (add field selectors, page with `limit`, watch instead of list, raise resync intervals), then give a genuinely important flow its own FlowSchema, and only then raise total concurrency where you control the flags.
- Client-side throttling is a different message (`client-side throttling, not priority and fairness`, from `--qps`/`--burst` in the client's rest config). Raising the server's limits does nothing for it.

## etcd

- etcd is the only stateful component, and it fails by filling up. Its own default storage quota is 2 GiB and the supported maximum is 8 GiB — past the quota, etcd raises a `NOSPACE` alarm and **the whole cluster goes read-only for writes** while reads keep working. The error is `etcdserver: mvcc: database space exceeded`.
- Recovery is three steps, in order: compact old revisions, defragment each member (it blocks that member for the duration — do them one at a time), then disarm the alarm. Deleting objects alone frees nothing, because the space is held by historical revisions.
- The API server requests compaction every 5 minutes by default (`--etcd-compaction-interval`); defragmentation is never automatic. A cluster that has run for a year without a defrag has a database several times larger than its data.
- What actually fills it: Events (high churn, and they are objects like everything else), large ConfigMaps and Secrets, thousands of custom resources, and Helm release Secrets accumulating one per revision. Moving Events to their own etcd (`--etcd-servers-overrides`) is the standard fix on self-managed clusters and is invisible to workloads.
- Object size: the practical ceiling for a single object is ~1.5 MiB (etcd's default max request size); ConfigMaps and Secrets cap at 1 MiB before that (`config-and-secrets.md`). CRDs are for configuration, never for application data (`operators.md`).
- Latency is the other failure: etcd needs low-latency fsync. `etcd_disk_wal_fsync_duration_seconds` p99 above ~10ms on spinning or network-throttled disks produces leader elections, and a leader election is a brief cluster-wide write outage.

## Certificates — The Cluster-Wide Expiry Class

Certificate expiry is the one failure that hits every node and every write simultaneously, and it is on a calendar you can read a year in advance.

| Certificate | Typical lifetime | What expiry does |
|---|---|---|
| Cluster CA | 10 years | Everything, permanently — plan the rotation, never discover it |
| API server, controller-manager, scheduler client certs | 1 year (kubeadm default) | Control plane components lose their own API access |
| kubelet client cert | 1 year, auto-rotates when `rotateCertificates` is on | Every node goes NotReady at once; the fix is CSR approval, not a reboot (`nodes.md`) |
| kubelet **serving** cert | Needs `serverTLSBootstrap` plus an approver | `kubectl logs`, `exec`, and metrics-server fail with x509 while pods are perfectly healthy |
| Webhook serving certs | Issuer-dependent | Every create fails at once (`operators.md`) |
| Ingress and mesh certs | 90 days with ACME | Traffic-facing only (`ingress.md`, `mesh.md`) |

- Pending CertificateSigningRequests are the tell: `kubectl get csr` full of `Pending` entries means nothing is approving them, and the cluster is quietly running on borrowed time.
- On kubeadm clusters, an expiration report exists as a first-class command; upgrading the control plane renews the component certificates as a side effect, which is why clusters upgraded yearly never see this and clusters frozen "for stability" do.
- Put the sweep in `## Due` with a real date. This is the canonical case where a calendar entry outperforms any amount of monitoring.

## Aggregated APIs and the Cluster That Half-Works

- An `APIService` (metrics.k8s.io, a custom aggregated API) that is `Available: False` breaks more than its own endpoint: `kubectl get all`, anything enumerating resources, and **namespace deletion** all hang or error, because the API server cannot list what it must delete (`operators.md`).
- One command settles it: list APIServices and look for anything not `True`. Fix the backing pods or delete the APIService; leaving it broken degrades unrelated work forever.

## Audit Logging

- Policy levels per rule: `None`, `Metadata`, `Request`, `RequestResponse`. Logging `RequestResponse` on everything is how an audit pipeline costs more than the cluster; `Metadata` on reads plus `Request` on writes to sensitive resources is the shape that stays affordable.
- Always exclude the high-volume noise: leases, endpointslices, and events. They are most of the write volume and none of the value.
- Ship it off-cluster. In-cluster logs are exactly what an attacker with cluster access deletes, and during an incident the cluster is where you cannot trust the record (`security.md`).
- On a managed control plane, audit and API server logs are an opt-in feature with its own bill. Enabling them during the incident produces nothing about what already happened — this is a before, not a during.

## Leader Election and the Components That Do Nothing

- controller-manager, scheduler, and every well-built operator hold a `Lease` and act only as leader. A component that runs, logs nothing interesting, and changes nothing is usually not the leader.
- Check the lease holder and its renewal time before debugging any controller's logic (`operators.md`).
- Frequent leader changes point at API latency or etcd, not at the component: renewals are API writes, and a slow control plane makes every component look flaky at once.

## Control-Plane Triage

1. `kubectl get --raw='/readyz?verbose'` — which check fails names the subsystem; `/livez` distinguishes "unhealthy" from "still starting".
2. `429` in the response, or throttling in controller logs → APF, above. Identify the flow before touching limits.
3. `504` or `etcdserver:` in the error text → etcd: space, latency, or quorum. `kubectl get --raw /metrics` still works when writes do not.
4. x509 errors anywhere → certificates, above. Check whether it is one component or all of them; all of them means a shared CA or a clock problem (`nodes.md`).
5. Namespaces stuck Terminating, or `kubectl get all` erroring → an unavailable APIService.
6. Everything fine but every create rejected → an admission webhook, not the control plane (`operators.md`).
7. Managed control plane and none of the above → open the provider's control-plane logs (enabling them now only helps next time) and check the provider's quota on API requests.

Write what this establishes into `## Clusters` in `~/Clawic/data/k8s/memory.md`: version, managed or self-managed, etcd size and last defrag, whether audit is shipped and where. Put every certificate expiry you discovered into `## Due` with its date — that table is the only thing standing between the user and a cluster-wide outage on a known calendar day.
