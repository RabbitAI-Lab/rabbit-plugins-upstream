# Service Mesh — Sidecars, mTLS, and the Failures They Add

A mesh moves retries, timeouts, encryption, and traffic splitting out of the application and into a proxy beside it. The trade is exact: every request now crosses two extra hops that the app team cannot read, and every pod carries a second process with its own lifecycle, memory, and upgrade schedule.

Before adopting one, read `## Clusters` in `~/Clawic/data/k8s/memory.md` — if a mesh is already installed, its flavor and mode decide half of this file, and if the decision was made before, `artifacts/` holds why.

## Is The Mesh Worth It Here

| You need | Cheaper way first | Mesh earns it when |
|---|---|---|
| Encryption in transit | TLS at the ingress; a compliance regime that says "in transit" often means "at the perimeter" | Auditors require pod-to-pod encryption, or the network is genuinely untrusted |
| Retries and timeouts | The client library, where the app knows what is idempotent | Polyglot fleet where no shared library exists |
| Traffic splitting for canaries | Gateway API `backendRefs` weights, or replica-ratio canaries (`rollouts.md`, `ingress.md`) | Per-request percentages below ~5%, or header-based routing |
| Golden metrics per service | Instrumentation, or an ingress controller's metrics | You need them for services nobody will instrument |
| Zero-trust authorization between services | NetworkPolicy at L3/L4 (`networking.md`) | Rules need identity and L7 verbs, not IPs |

Honest threshold: below roughly a dozen services, with no compliance requirement for in-cluster encryption, the mesh costs more than it returns. The cost is not the install — it is that every future incident has one more layer, and the layer speaks Envoy.

## Sidecar Mode vs Ambient Mode

- **Sidecar** (Istio classic, Linkerd): a proxy container is injected into every pod and iptables rules in an init container redirect all traffic through it. Full L7 features everywhere, and per-pod memory and CPU overhead on every workload — including the ones that never needed it.
- **Ambient** (Istio): a per-node L4 component handles mTLS for everything, and L7 features require an explicitly deployed waypoint proxy per namespace or service. Cheaper by default, and the L7 features you want are opt-in rather than ambient — verify the feature set on the version you would actually run before committing.
- **Linkerd**: a deliberately smaller proxy with mTLS on by default and far fewer knobs. The knobs are the point of Istio and the cost of Istio; choose accordingly.
- Injection is namespace- or pod-labelled. The most common "why is there no sidecar" is a pod created before the namespace was labelled: injection happens at admission, so existing pods keep running unmeshed until they are recreated.

## The Sidecar Lifecycle Problems

These are the failures that belong to the mesh and not to your app:

- **Jobs that never complete.** A classic sidecar keeps running after the main container exits, so the pod stays `NotReady` forever and the Job never reaches Completed (`jobs.md`). Three fixes, best first: native sidecars (an initContainer with `restartPolicy: Always`, which the kubelet terminates *after* the app containers, GA on recent versions — verify on the cluster), the mesh's own shutdown endpoint called from the job's last line, or excluding batch namespaces from injection entirely.
- **Startup races.** The app container can start before the proxy is ready and its first outbound connection is refused. Native sidecars fix the ordering by construction; Istio's `holdApplicationUntilProxyStarts` does it in the classic model. A retry loop in the entrypoint is the workaround people ship instead, and it hides the problem in the logs.
- **Shutdown ordering, in reverse.** If the proxy dies first, in-flight requests fail during every rollout. The `preStop` sleep of Core Rule 5 has to exist on the proxy as well as on the app; native sidecars make this ordering the default.
- **PSA conflicts.** The traffic-capture init container needs `NET_ADMIN`, which a `restricted` namespace rejects. The CNI-plugin mode of injection avoids the init container entirely — the correct answer when `psa_level: restricted` (`security.md`).
- **Probes.** Kubelet probes come from the node, outside the mesh, so STRICT mTLS would fail them; meshes rewrite probe paths through the proxy to compensate. When that rewrite is disabled, every pod goes unready at once the moment STRICT is enabled (`probes.md`).

## mTLS Without An Outage

- Modes are per-workload and per-port: `PERMISSIVE` accepts both plaintext and mTLS, `STRICT` accepts only mTLS. Migration order is always the same: mesh everything, leave PERMISSIVE, confirm from telemetry that no plaintext traffic remains, then flip STRICT namespace by namespace.
- The signature of flipping too early: `upstream connect error` or `503 UF/URX` from a caller that is not in the mesh — an unmeshed CronJob, a monitoring scraper, or a pod in a namespace nobody labelled.
- **mTLS is authentication, never authorization.** With mTLS on and no authorization policy, every meshed workload can still call every other one; it is now merely encrypted. The authorization objects are separate, and their default is allow.
- Traffic that never enters the mesh: anything using `hostNetwork`, node-level agents (`daemonsets.md`), and direct pod-IP calls that bypass the Service. Do not claim "all traffic is encrypted" until those three are accounted for.

## Protocol Detection, The Silent Feature Loss

- Meshes decide L7 behavior from the Service port's name or `appProtocol`. An unnamed port is treated as opaque TCP: no retries, no per-route timeouts, no HTTP metrics, and no obvious error. The service simply behaves as if the mesh were not there.
- Name ports `http`, `http2`, `grpc`, `tls`, or set `appProtocol` explicitly (`networking.md`). This is the most common reason a mesh "does not seem to be doing anything".
- Headless Services and client-side load balancing interact badly with proxies that expect a VIP; gRPC over a headless Service is the usual case, and it needs deliberate configuration rather than defaults (`dns.md`).

## Retries and Timeouts Are Now Multiplicative

- A mesh retry policy applies at every hop. Three services deep with 3 attempts each is up to 27 requests reaching the bottom service from one client call — the mesh turns a slow dependency into a self-inflicted load test.
- Set retries at the edge only, cap them with a budget, and never retry non-idempotent verbs by default.
- Timeouts stack with the ingress controller's read timeout and the application's own (`ingress.md`). The mesh's per-route timeout must sit inside the ingress timeout, not outside it, or the client sees the ingress error and the mesh's carefully chosen value never applies.
- Circuit breaking (connection pool limits plus outlier detection) is the part of a mesh that genuinely prevents cascading failure, and the part teams configure last.

## Operating It

- The control plane is a cluster-wide dependency: its outage does not drop existing traffic (proxies keep their last configuration) but nothing new can be configured and new pods may fail to start. Run it with multiple replicas and a PDB, like any other cluster-wide component (`production.md`).
- Data-plane upgrades require restarting every meshed pod — a fleet-wide rolling restart with all the PDB and capacity consequences of one (`rollouts.md`). Control plane and proxies are supported within a limited version skew, so the restart is not optional and the maintenance window has to be sized for the whole fleet.
- Debug from the proxy, not the app: proxy configuration dump and sync status tell you whether this pod ever received the route you wrote, which is the difference between a config bug and a mesh bug. Envoy access logs carry response flags (`UF`, `URX`, `NR`, `UO`) that name the failure class precisely.
- Resource cost is per pod and real: budget proxy CPU and memory into every workload's requests, then re-check the cluster's requested-versus-allocatable ratio (`resources.md`, `production.md`). A mesh across 400 pods is a node group nobody planned.

## Mesh Triage

| Symptom | Cause | Move |
|---|---|---|
| Job pods stay NotReady after finishing | Sidecar never exits | Native sidecar, or exclude batch from injection |
| App's first outbound call fails at boot | Proxy not ready yet | Startup ordering, above |
| `503 UF` / `upstream connect error` between healthy pods | STRICT mTLS with an unmeshed caller, or a policy denying it | PERMISSIVE, find the caller in telemetry, then re-flip |
| No metrics, no retries, no timeouts on one service | Port not named, no `appProtocol` | Protocol detection, above |
| Every pod unready right after enabling STRICT | Probe rewriting disabled | Probes, above |
| Latency up ~1-3ms per hop after adoption | The two extra hops — expected | Decide whether the trade still holds; the decision goes to `artifacts/` |
| A route works in one namespace only | Policy or route scoped to a namespace, or waypoint missing in ambient mode | Proxy config dump on both sides |
| No sidecar in a pod | Namespace labelled after the pod was created | Recreate the pod |

Write the outcome where it survives the session: the mesh flavor, mode, version, and mTLS posture go in `## Clusters`; the adoption or rejection decision, with what it was traded against, goes in `~/Clawic/data/k8s/artifacts/decision-<kebab>.md` with its `## Boxes` line — this is the decision most likely to be re-litigated in six months by someone who was not there.
