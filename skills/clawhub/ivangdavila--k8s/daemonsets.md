# DaemonSets — The Agents On Every Node

A DaemonSet is the only workload whose blast radius is the entire fleet by construction: one pod per node, updated node by node, usually holding privileges no application pod is allowed. CNI, kube-proxy, CSI node plugins, log shippers, metrics agents, security sensors, and device plugins all arrive this way (`gpu.md`).

Two consequences run through everything below: a bad DaemonSet update degrades every node, and the agents are exactly the pods you need alive when the node is in trouble.

## Coverage Is The Whole Point, And It Fails Silently

- `DESIRED` versus `READY` on `kubectl get ds -A` is the only health question that matters. A log shipper missing on three nodes produces no error anywhere — just a silent hole in the logs that is discovered during an incident.
- The scheduler places DaemonSet pods with node affinity, so ordinary scheduling failures apply: a node whose resources are fully requested by application pods has no room for a new agent, and the agent is what you needed (`scheduling.md`).
- **`system-node-critical` exists for this.** Genuine node infrastructure gets that PriorityClass so it can preempt application pods rather than queue behind them. Handing it to a non-essential agent is the mirror mistake: now a log shipper evicts production (`scheduling.md`).
- Tolerations decide coverage. A DaemonSet reaches a tainted pool only if it tolerates that taint — GPU, spot, and infra pools each need an explicit toleration, and "the agent is missing on the GPU nodes" is nearly always this.
- The controller adds tolerations for node lifecycle conditions (not-ready, unreachable, memory/disk/PID pressure, unschedulable) so agents keep running on a sick node. That is deliberate: the log shipper must survive DiskPressure long enough to explain it (`nodes.md`).

## Sizing Agents Is Not Like Sizing Apps

- An agent's load scales with **node size and pod density**, not with a fixed request. The same log shipper needs several times more memory on a 64-core node running 200 pods than on a 4-core node running 12.
- Size from the biggest node in the fleet, and re-check after any node-class change. The classic failure is an agent with a 100Mi limit that OOM-loops only on the large pool — and OOM-looping agents are indistinguishable from "logs are a bit late".
- Multiply before accepting a request: 100m CPU × 200 nodes is 20 cores of the cluster permanently spent on one agent. Agent overhead is real capacity and belongs in the capacity calculation (`production.md`).
- Memory request = limit applies here too (Core Rule 1) — an agent in the Burstable class is an early eviction candidate on precisely the node under pressure.

## Rolling An Update Across Every Node

- Default `maxUnavailable: 1` means a 200-node fleet is 200 sequential steps. `maxSurge` (where the agent tolerates two instances briefly) parallelizes it; raising `maxUnavailable` is the blunt version and should be a deliberate decision, not a default (`rollouts.md`).
- `updateStrategy: OnDelete` is the right choice for the agents whose failure takes the node with them — CNI above all. Nothing changes until you delete a pod, which turns the rollout into a manual canary you control node by node.
- Canary by node label: patch a `nodeSelector` or use a separate DaemonSet targeting one label value, verify on a handful of nodes, then widen. A DaemonSet has no revision-based canary of its own.
- Rollback works (`kubectl rollout undo` on a DaemonSet honors `revisionHistoryLimit` the same way) but it is another full pass across the fleet. Time both directions before starting.
- Node agents are also what a node upgrade replaces first: on cordon-and-replace pools, the new node comes up with whatever version the DaemonSet currently specifies, so a half-finished rollout plus node churn leaves a fleet on two versions indefinitely (`nodes.md`).

## Privileges, Legitimately

- This is the one workload class where `hostNetwork`, `hostPID`, `hostPath`, and specific capabilities are a design rather than a finding — a CNI agent cannot do its job inside a pod network namespace.
- Make the exception visible: a dedicated namespace labelled `pod-security.kubernetes.io/enforce: privileged`, one ServiceAccount per agent, and the narrowest capability set that works instead of `privileged: true` (`security.md`).
- Audit what they can read. An agent mounting `/var/lib/kubelet` can read every pod's Secrets on that node, and its ServiceAccount is often cluster-wide read. A compromised logging agent is a cluster-wide credential compromise (`rbac.md`).
- Prefer `hostPath` mounts as `readOnly` wherever the agent only observes, and pin the paths — `/var/log/pods` and `/var/lib/docker/containers`, never `/`.

## Drains, Evictions, and Why Drain Ignores Them

- `kubectl drain` requires `--ignore-daemonsets` because evicting a DaemonSet pod is pointless: the controller recreates it on the same node immediately. The agents keep running while everything else leaves, which is what you want during a drain (`nodes.md`).
- The corollary for the cluster autoscaler: DaemonSet pods never block scale-down, but they do consume allocatable on every node, including nodes the autoscaler is deciding about. Ten agents at 100Mi each is a gigabyte per node that no application can use (`autoscaling.md`).
- A DaemonSet pod that cannot terminate blocks node deletion in some managed pools. Give agents a real `preStop` and a grace period sized to their flush time — a log shipper killed at SIGTERM loses the buffered logs from the incident you are draining the node for (`probes.md`).

## DaemonSet Or Sidecar

| Question | DaemonSet | Sidecar |
|---|---|---|
| Cost model | Per node | Per pod — the same agent × every replica |
| Isolation | One tenant's agent failure affects the node | Per workload |
| Configuration | Fleet-wide, one place | Per workload, per team |
| Access to app internals | Only what the node exposes (stdout, files, /proc) | Anything in the pod's namespaces |
| Typical fit | Log collection from stdout, node metrics, CNI, CSI, device plugins | Application-specific export, mesh proxies (`mesh.md`), per-tenant credentials |

Default to DaemonSet for anything node-shaped: at 200 pods per node the sidecar version costs 200× the memory for the same job. Reach for a sidecar when a workload needs different configuration than the fleet, or when the data never reaches the node's stdout.

## Static Pods Are Not DaemonSets

- Static pods are defined by files in the kubelet's manifest directory and run without the API server's involvement — which is how a self-managed control plane bootstraps itself (`control-plane.md`).
- They appear in the API as mirror pods that cannot be edited or deleted through kubectl; the file on the node is the source of truth, and editing the mirror does nothing.
- Anything that is not control-plane bootstrap belongs in a DaemonSet, where it is versioned, reviewable, and rolled out under your control.

## DaemonSet Triage

| Symptom | Cause | Move |
|---|---|---|
| `DESIRED` > `READY`, no obvious errors | Pods Pending on some nodes: no room, or no toleration for that pool | `kubectl get pods -o wide` against the node list; then `scheduling.md` |
| Agent missing entirely on one pool | Untolerated taint, or a nodeSelector excluding it | Tolerations, above |
| Agent OOM-loops only on the large nodes | Sized from the small pool | Size from the biggest node, above |
| Rollout crawling for hours | `maxUnavailable: 1` across N nodes | `maxSurge`, or a deliberate raise |
| Node upgrade left two agent versions running | Rollout overlapped with node replacement | Complete the rollout, then re-check per-node versions |
| Every node degraded right after an agent update | Fleet-wide blast radius, as designed | Roll back, then re-ship with `OnDelete` or a node-label canary |
| Logs missing for a window nobody noticed | Agent unready or evicted during that window | Alert on unavailable-count, not on agent errors |
| Agent cannot start after a node reboot | hostPath that no longer exists, or SELinux labelling | Node-level, not manifest-level (`nodes.md`) |

Record the agent inventory — which DaemonSets run on which pools, their versions, and the per-node overhead they add — in `## Clusters` in `~/Clawic/data/k8s/memory.md`. It is the number every capacity estimate forgets, and the list every upgrade plan needs.
