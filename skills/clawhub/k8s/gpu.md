# GPUs and ML Workloads — Accelerators That Actually Get Scheduled

GPUs enter Kubernetes as an **extended resource** advertised by a device plugin, not as something the scheduler understands natively. Everything strange about GPU scheduling follows from that: the resource is opaque, integral, and unenforced.

Read `## Clusters` in `~/Clawic/data/k8s/memory.md` before sizing anything — which accelerator pools exist and whether sharing is enabled changes every number below — and `## Workloads` for model load times already measured.

## The Rules That Differ From CPU and Memory

- Requests must be **integers**, and request must equal limit. There is no fractional GPU in core Kubernetes and no `limits.gpu-memory` field at all.
- The GPU count is advertised by a device plugin DaemonSet (`daemonsets.md`). If that pod is not running and healthy on a node, the node advertises zero GPUs and your pod stays Pending next to idle hardware.
- **GPU memory is not cgroup-managed.** Two pods sharing one GPU can exhaust each other's memory; the failure surfaces as a CUDA out-of-memory error inside the application, never as an OOMKill Kubernetes can attribute.
- Extended resources are not overcommittable and not preemptible in any useful sense: a GPU pod either gets a whole device or waits.
- Nodes with accelerators cost 10-40× a general-purpose node of the same core count. Everything about GPU cluster design is really about keeping them busy.

## Getting A Pod Onto A GPU

1. **Taint the pools, tolerate deliberately.** Untainted GPU nodes fill with ordinary pods that then block a training job from scheduling — the most expensive idle capacity in the cluster (`scheduling.md`).
2. **Select the hardware, not just the count.** Node labels published by the device plugin (product name, memory size, MIG profile, driver version) are what distinguishes an accelerator that will run your model from one that will not. `nvidia.com/gpu: 1` alone lets the scheduler hand you the wrong generation.
3. **The runtime class matters.** Container access to devices depends on the node's container runtime being configured for it. A pod that starts, sees no device, and fails inside CUDA usually has the wrong (or a missing) `runtimeClassName`.
4. **Driver, toolkit, and image must agree.** The kernel driver lives on the node, the container toolkit exposes devices into the container, and CUDA lives in the image. Drivers support their own CUDA version and older ones, never newer: a newer CUDA image on an older driver fails at runtime, not at admission. A GPU operator exists precisely to keep those three in step, and hand-managed nodes drift.

## Sharing One GPU

| Strategy | How it divides | Isolation | Use for |
|---|---|---|---|
| Exclusive (default) | One pod, one device | Complete | Training, latency-sensitive inference |
| Time-slicing | The plugin advertises N virtual devices; the driver context-switches | **None** — shared memory, shared faults, no fairness guarantee | Dev, notebooks, bursty low-stakes inference |
| MIG (hardware partitioning) | The device is split into fixed profiles advertised as separate resources | Memory and compute isolated in hardware | Multi-tenant inference on data-center cards |
| MPS | Concurrent kernels from multiple processes | Partial | Small kernels that individually underuse the device |

- Time-slicing changes the advertised count, so a node "has" 8 GPUs and a scheduler that believes it. Latency becomes unpredictable and one pod's OOM can take out its neighbors. Never enable it on a pool that serves a latency SLO.
- MIG profiles are configured per node and changing them requires draining the node. Decide the profile mix per pool, not per workload, and record it in `## Clusters`.

## Training Workloads

- **`/dev/shm` defaults to 64 MB in a container**, and PyTorch DataLoader workers communicate through it. The symptom is a training job that dies with a bus error or a vague worker-crash message at a random epoch. Fix: an `emptyDir` with `medium: Memory` mounted at `/dev/shm` with a `sizeLimit` — and remember tmpfs counts against the pod's memory limit (`resources.md`).
- **Multi-node training needs gang scheduling, which core Kubernetes does not have.** A distributed job whose pods schedule one by one holds expensive GPUs idle while waiting for the last rank, and can deadlock two jobs against each other permanently. Use a batch scheduler or queueing layer that reserves all-or-nothing; without one, cap distributed jobs at one node.
- Inter-node bandwidth decides scaling efficiency: collective operations are bandwidth-bound, and standard pod networking with overlay encapsulation is the wrong substrate for it (`networking.md`). High-speed fabrics arrive as their own device-plugin resources that must be requested alongside the GPU.
- Checkpoint on a schedule sized to the interruption risk, not to the epoch: on spot accelerators the notice is 30-120 seconds (`nodes.md`), which is enough to stop cleanly only if a checkpoint is already recent.
- `activeDeadlineSeconds` and `podFailurePolicy` matter more here than anywhere: a hung training pod holds four figures a day of hardware and no retry counter advances (`jobs.md`).

## Inference Workloads

- **Model load time dominates startup.** Tens of gigabytes of weights pulled from object storage or a registry turn a "slow boot" into minutes. Size the startupProbe budget from a cold pull, never from a warm node (Core Rule 2), and expect the first pod on a new node to be several times slower than the rest.
- That startup cost is also the autoscaling cost: scale-up latency is the pull plus the load, so HPA on a GPU service needs headroom, not reaction (`autoscaling.md`). Scale-to-zero is only viable where a multi-minute first request is acceptable.
- Batching is the throughput lever, and it trades latency for it. Autoscale on queue depth or in-flight requests rather than on GPU utilization, which saturates long before the service does.
- Cache weights on the node (a pre-pull DaemonSet, a shared read-only volume, or a local disk cache) when the same model lands on new nodes repeatedly.

## Keeping Them Busy

- Utilization is the only cost lever that matters: an idle GPU costs the same as a saturated one. Export per-device utilization and memory (a DCGM-class exporter runs as a DaemonSet) and treat a pool below ~40% average as a consolidation problem, not a capacity problem.
- Separate pools by workload class — interactive notebooks, batch training, production inference — and give batch a lower PriorityClass with `preemptionPolicy: Never` so it queues behind production without evicting it (`scheduling.md`).
- Notebooks are the canonical waste: a human opens one, walks away, and holds a device overnight. A TTL controller or an idle-culling policy on the notebook platform pays for itself in a week.
- Cluster autoscaling on GPU pools is slow (large images, driver installation) and quota-limited by the provider. Request quota before the project, not during it.

## GPU Triage

| Symptom | Cause | Move |
|---|---|---|
| Pod Pending, `Insufficient nvidia.com/gpu`, nodes look free | Device plugin not running, or the node has not registered its devices yet | `kubectl describe node` — is the resource advertised at all? Then the plugin DaemonSet (`daemonsets.md`) |
| Pod Pending with no obvious predicate on a tainted pool | Toleration missing, or nodeSelector naming a label no node carries | `scheduling.md` |
| Pod runs, `nvidia-smi` shows nothing | Runtime class or toolkit not configured on that node | Compare with a working node; it is node config, not the manifest |
| CUDA version / driver mismatch error at startup | Image's CUDA newer than the node's driver | Pin the image to the fleet's driver, or upgrade drivers first |
| Random worker crashes during data loading | `/dev/shm` at 64 MB | tmpfs `emptyDir` at `/dev/shm`, above |
| Out-of-memory inside CUDA while the pod is well under its memory limit | GPU memory, which the limit does not cover — often a co-tenant under time-slicing | Exclusive device or MIG |
| Distributed job hangs with some ranks running | Partial scheduling, no gang guarantee | Gang scheduler, or single-node |
| First request after scale-up times out | Model load, not inference | Startup budget and warm pools, above |
| Utilization near zero on a busy-looking cluster | Pods holding devices they are not using | Per-device metrics, then idle culling |

Write what this session established into memory: accelerator pools, sharing mode, MIG profiles and driver version go in `## Clusters`; measured model load time, cold-pull time, per-pod GPU count and checkpoint interval go in the workload's row in `## Workloads` — those cost a full training run each to discover.
