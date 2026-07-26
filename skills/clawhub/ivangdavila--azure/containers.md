# Containers — AKS, Container Apps, ACI and the Registry

Three ways to run a container, and the choice is mostly about how much Kubernetes you actually need. The registry and its authentication path are the part everyone forgets until a pull fails at 2am.

**Contents:** [Choosing the Host](#choosing-the-host) · [Container Apps](#container-apps) · [AKS Cluster Design](#aks-cluster-design) · [AKS Networking and IP Math](#aks-networking-and-ip-math) · [AKS Upgrades and Version Support](#aks-upgrades-and-version-support) · [AKS Cost Control](#aks-cost-control) · [ACR and the Pull Path](#acr-and-the-pull-path) · [ACI](#aci) · [Failure Signatures](#failure-signatures)

## Choosing the Host

| | Container Apps | AKS | ACI |
|---|---|---|---|
| Control plane to operate | None | Yours, including upgrades | None |
| Scale to zero | Yes | Only with extra components | Per container group |
| Kubernetes API | No | Yes | No |
| Ingress, revisions, blue/green | Built in | You build it | None |
| Right when | Microservices, jobs, event-driven work with no operator requirements | Operators, CRDs, service mesh, multi-tenant namespaces, existing manifests | Burst capacity, one-off jobs, sidecar-free simple tasks |

Break-even to state out loud: AKS charges an uptime-SLA control plane plus a node pool that must be big enough for the system pods before your workload gets a core. Below roughly four always-on containers with no Kubernetes-specific requirement, Container Apps is cheaper and dramatically less work. Above it, or the moment a requirement names a CRD, AKS is not a preference (`services.md`).

## Container Apps

- Runs on Kubernetes and KEDA underneath, but the API is the app, not the cluster. Scaling rules are KEDA scalers: HTTP concurrency, queue length, CPU, cron, or any supported source.
- **Scale to zero** applies to HTTP and event-driven apps; min replicas above zero removes cold start and the savings together.
- **Revisions** are immutable snapshots of an app version; traffic splitting across revisions gives canary and blue/green without another product.
- Environments are the network and observability boundary — apps in one environment share a VNet subnet (delegated, and sized generously) and a Log Analytics workspace. Plan the subnet before creating the environment; it cannot be changed afterwards.
- Jobs (scheduled, event-driven, manual) cover the batch cases that would otherwise justify a cluster.
- Dapr is optional and useful for service invocation, pub/sub and state; adopting it is an application-architecture decision, not an infrastructure toggle.
- Limits worth naming: replicas per app, concurrent requests per replica, and the environment's subnet size. State the first one the design will hit.

## AKS Cluster Design

- **System and user node pools are separate for a reason.** System pods (CoreDNS, metrics server, CSI drivers) belong on a small system pool with a taint; workloads go on user pools. A cluster with one pool eventually evicts CoreDNS to schedule a batch job.
- Node pool per workload shape: general, memory-heavy, GPU, spot. Taints and tolerations, not hope, keep things where they belong.
- **Cluster autoscaler** scales node pools; the **horizontal pod autoscaler** scales pods. Both are needed, and pods that request no resources make the autoscaler blind — resource requests are the input to every scheduling decision.
- Pod Disruption Budgets are what make node drains safe during upgrades and scale-in. A PDB that can never be satisfied blocks upgrades forever, which is its own failure mode.
- Availability zones are chosen per node pool at creation. A zonal outage without zone-spread node pools is a cluster outage.
- **Disable local accounts and use Entra ID with Kubernetes RBAC**, otherwise a subscription Contributor can pull admin credentials and bypass every in-cluster rule (`identity.md`).
- Workload identity (federated credentials on a service account) is the current mechanism for pods to authenticate to Azure. The older pod-identity mechanism is gone; anything still using it is a migration item.

## AKS Networking and IP Math

This is the constraint that stops clusters from scaling, and it is decided at creation.

- **Azure CNI (node subnet)**: every pod gets a real VNet IP. Required subnet size is `nodes × (max_pods + 1)`, computed for the **maximum** the autoscaler may reach, plus room for upgrade surge nodes. A `/24` with `max_pods` at 30 supports about 8 nodes — a number most teams discover at the worst moment.
- **Azure CNI Overlay**: pods get addresses from a separate overlay space, nodes take VNet IPs. This removes the IP ceiling for almost all designs and is the sensible default now.
- **kubenet** is legacy; route-table limits and NAT behaviour make it a poor choice for new clusters.
- Network plugin and pod CIDR cannot be changed after creation. Migrating means a new cluster.
- **Outbound**: the default load-balancer outbound path gives each node a small SNAT port allocation, and a chatty cluster exhausts it. Attach a NAT Gateway to the node subnet for anything that makes many outbound connections (`networking.md`).
- Network policies (Azure or Cilium) must be enabled at creation to be available later.
- Private clusters put the API server behind a private endpoint, which means CI must have a network path to it — decide before, not after, the pipeline breaks.

## AKS Upgrades and Version Support

- Kubernetes minor versions leave support roughly twelve months after their GA; long-term support tiers extend that at a higher control-plane price. An unsupported cluster stops receiving fixes and cannot open a support case on the version.
- **Put the support-end date in `## Due`** the moment a cluster is created or upgraded (`memory-template.md`). "Upgrade AKS" without a date is a task that arrives as an incident.
- Upgrade order: control plane first, then node pools. Skipping minor versions is not allowed — upgrading two minors is two upgrades.
- Node image upgrades are separate from Kubernetes upgrades and carry the OS security patches. Automatic node image upgrade with a maintenance window is the low-effort correct default.
- Surge settings control how many extra nodes appear during an upgrade: higher surge is faster and needs both IP space and quota. This is where an IP-tight subnet fails an upgrade.
- Test upgrades on a non-production cluster with the same add-ons; the add-ons are what break, not the API.

## AKS Cost Control

- The Free control-plane tier has no uptime SLA; the Standard tier charges per cluster-hour for one. Non-production clusters rarely need it.
- Node pools are VMs: everything in `vms.md` about families, right-sizing, spot and ephemeral OS disks applies, and ephemeral OS disks are the default worth using for stateless nodes.
- Spot node pools with a taint, plus an on-demand base pool, is the standard cost pattern for batch and CI.
- Cluster stop/start exists for dev clusters — a stopped cluster does not bill for nodes.
- **AKS container stdout is the single largest Log Analytics ingestion source on most estates.** Container Insights collects everything by default; a data collection rule that excludes noisy namespaces and drops verbose columns typically cuts the bill by more than any node right-sizing (`monitoring.md`).

## ACR and the Pull Path

- Tiers: Basic (small), Standard (most), Premium (private endpoints, geo-replication, higher throughput and larger concurrent pull capacity). Private networking requires Premium — a fact that reshapes the design when the security review lands.
- **Authentication should be identity-based**: attach the registry to the cluster so the kubelet identity has `AcrPull`, or assign `AcrPull` to the workload identity. Admin user and registry passwords are the fallback that ends up in a git repository.
- The pull path must resolve and route: with a private endpoint, the cluster needs the `privatelink.azurecr.io` zone linked to its VNet, and Premium's data endpoints need their own DNS entries (`networking.md`).
- Retention: untagged manifests accumulate silently. A retention policy on untagged manifests is free housekeeping; without it, storage grows forever.
- Geo-replication puts a replica in each region that pulls, which is both a latency and an egress-cost decision.
- Image tags are mutable by default. For anything production, deploy by digest and record the digest in `deploys/<year>.md` — a rollback target that says `:latest` is not a rollback target (`memory-template.md`).

## ACI

- Per-second billing, no orchestration, no autoscaling, no health-based restarts beyond a restart policy.
- Correct for: short jobs, burst capacity behind Container Apps or AKS virtual nodes, isolated tasks with a VNet requirement.
- Wrong for: anything long-running that needs to stay healthy. There is no scheduler watching it.
- Start latency scales with image size; a multi-gigabyte image makes ACI feel broken.

## Failure Signatures

| Symptom | Cause | Fix |
|---|---|---|
| `ImagePullBackOff` / `ErrImagePull` | Registry auth, DNS to a private registry, or a tag that does not exist | Attach ACR or assign `AcrPull`; resolve the registry FQDN from a node |
| Pod `Pending` forever | No node has room for the resource requests, or a taint/nodeSelector matches nothing | Describe the pod: the scheduler states the reason |
| `CrashLoopBackOff` | Application failure, missing configuration, or a probe killing a slow starter | Logs of the previous container; check the startup probe's grace |
| Node `NotReady` after an upgrade | Node image, CNI or an add-on incompatible with the new version | Cordon, drain, replace the node; check add-on versions |
| Cluster cannot scale out | Subnet IP exhaustion, vCPU quota, or zonal capacity | The IP math above; then `vms.md` capacity errors |
| Intermittent outbound failures at load | SNAT exhaustion on the default outbound path | NAT Gateway on the node subnet |
| Container App revision stuck at 0 replicas | Scale rule never triggers, or min replicas is 0 and nothing is calling it | Check the scaler's source and its authentication |
| Everything works, Log Analytics bill triples | Container Insights collecting all stdout | DCR filtering (`monitoring.md`) |

**When a cluster or environment is created or resized, record it** in `## Current Infrastructure` — cluster name, node pools with sizes and counts, network plugin, Kubernetes version — and put the version support-end date in `## Due`. AKS node pools that the user manages as machines also earn a row in `~/Clawic/data/servers/servers.md` (`memory-template.md`).
