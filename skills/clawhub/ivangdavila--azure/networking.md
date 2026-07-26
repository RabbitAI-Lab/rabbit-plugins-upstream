# Networking — VNets, Private Link, and Traffic That Goes Nowhere

Azure networking fails quietly: the resource is created, the deployment succeeds, and the traffic goes to the wrong place. Work the path in order, never by guess.

**Contents:** [Address Planning](#address-planning) · [The Path Checklist](#the-path-checklist) · [NSGs and ASGs](#nsgs-and-asgs) · [Private Endpoints and DNS](#private-endpoints-and-dns) · [Service Endpoints](#service-endpoints) · [Outbound Connectivity and SNAT](#outbound-connectivity-and-snat) · [Peering, Hubs and Routing](#peering-hubs-and-routing) · [Load Balancing Front Doors](#load-balancing-front-doors) · [Hybrid Connectivity](#hybrid-connectivity) · [DNS Inside a VNet](#dns-inside-a-vnet)

**Before designing any subnet, peering, gateway or private endpoint**, read the address plan named in `## Boxes` of `~/Clawic/data/azure/memory.md` (`artifacts/address-plan.md`). Overlapping ranges are discovered at peering time, when both sides are already in production.

**After allocating any range, creating a peering, or reserving space for a future spoke**, write it back to `artifacts/address-plan.md` — creating the file with its `## Boxes` line if it does not exist yet (`memory-template.md`).

## Address Planning

- Azure reserves **5 addresses per subnet**: the network address, the first three usable-looking ones (gateway plus two for Azure services), and the broadcast address. A `/29` yields 3 usable addresses, a `/24` yields 251.
- **Address space cannot overlap anything you will ever peer with**, including on-prem, partners, and the acquisition nobody has told you about. Reserve generously: an unused `/16` costs nothing, and re-addressing a live VNet is a migration.
- A VNet's address space can gain prefixes, but **a subnet in use cannot shrink** and resizing requires the subnet to be empty of certain resource types.
- Subnets with mandatory names and sizes: `AzureFirewallSubnet` (/26 minimum), `AzureFirewallManagementSubnet` (/26, forced-tunnelling designs), `GatewaySubnet` (/27 is the practical floor), `AzureBastionSubnet` (/26), `RouteServerSubnet` (/27). Application Gateway v2 wants its own subnet sized for autoscale — /24 is the size that stops being a problem.
- Delegated subnets (Container Apps, App Service integration, Flexible Server, NetApp) cannot host anything else. Plan them as separate ranges from the start.
- Private endpoints consume one IP each, and estates accumulate dozens. Give them a dedicated subnet per spoke with room to triple.

## The Path Checklist

Run in this order for "cannot reach X". Each step is a check, not a guess.

1. **Name resolution** — from *inside* the source subnet, resolve the target FQDN. A public IP for a Private Link service means the DNS chain is broken; everything below is irrelevant until it returns a private address.
2. **Effective security rules** on the source NIC (`az network nic list-effective-nsg`). This flattens subnet and NIC NSGs into what actually applies.
3. **Effective routes** on the source NIC. A user-defined route pointing at a firewall or a gateway that no longer exists is a silent black hole.
4. **Destination NSG or subnet rules** — inbound is evaluated subnet-then-NIC, outbound NIC-then-subnet.
5. **The service's own firewall** — Storage, SQL, Key Vault, Cosmos all have one, and "selected networks" excludes anything you did not list, including the portal.
6. **The listener** — is anything actually bound to that port on the target, and is the health probe passing?
7. **SNAT and idle timeouts** if the failure is intermittent or only under load (below).

Connection troubleshooter and NSG flow logs give ground truth when this ladder does not settle it.

## NSGs and ASGs

- Rules evaluate by **priority, lowest number first**, and the first match wins. Custom rules live in 100-4096; platform defaults sit at 65000+ and always lose to a custom rule — including the default that allows VNet-internal traffic, which a broad custom deny will silently kill.
- An NSG can be attached to a subnet, a NIC, or both. Both are evaluated: **inbound subnet → NIC, outbound NIC → subnet**. A rule that "should work" often loses to the other attachment point.
- **Service tags** (`Storage`, `AzureActiveDirectory`, `AzureMonitor`, `Internet`, `VirtualNetwork`, `AzureLoadBalancer`) beat hard-coded IP lists: Microsoft maintains the ranges. Regional variants (`Storage.westeurope`) narrow the grant.
- **Application security groups** let rules reference workload identity rather than addresses: `web-asg → db-asg on 5432`. This is what makes rules survive re-addressing.
- **168.63.129.16** is the platform address that serves DNS, health probes and host communication. Blocking outbound to it breaks load-balancer probes, DHCP renewal and agent heartbeats in ways that look like application failures. Allow `AzureLoadBalancer` inbound.
- NSGs do not filter private-endpoint traffic unless network policies are enabled on the subnet. If you assumed the NSG was protecting a private endpoint, verify that setting.
- NSG flow logs land in a storage account and analyse in Traffic Analytics — turn them on before you need them, since they record nothing retroactively.

## Private Endpoints and DNS

The single most common Azure networking failure: the private endpoint exists, and the application still connects over the public internet — or fails.

How it works: the endpoint gives the PaaS resource a private IP in your subnet. The resource's public FQDN (`account.blob.core.windows.net`) must resolve to that IP, which happens through a CNAME into a **privatelink zone** that you host privately.

1. Create the private endpoint in the right subnet.
2. Create the Private DNS zone with the **exact** name for that service — `privatelink.blob.core.windows.net`, `privatelink.database.windows.net`, `privatelink.vaultcore.azure.net`, `privatelink.azurewebsites.net`, `privatelink.documents.azure.com`, `privatelink.azurecr.io`. A near-miss silently does nothing.
3. **Link the zone to every VNet that must resolve it**, not just the one holding the endpoint. This is the step that is missed.
4. Register the endpoint's A record in the zone (automatic with a DNS zone group; manual otherwise, and manual records go stale when the endpoint is recreated).
5. If the VNet uses **custom DNS servers**, they must forward to 168.63.129.16 or to an Azure DNS Private Resolver — otherwise the private zone is never consulted. Custom DNS is the second most common cause.
6. For on-prem resolution, forward the privatelink zones to a resolver inside Azure. On-prem cannot see private zones by itself.

Then disable public network access on the resource. A private endpoint that leaves the public endpoint open has changed the route, not the exposure.

## Service Endpoints

The older mechanism, and not a replacement for private endpoints.

| | Service endpoint | Private endpoint |
|---|---|---|
| Address | Public IP, traffic stays on the Azure backbone | Private IP in your subnet |
| Grants access to | The **entire service** in the region, restricted to your subnet as source | One specific resource instance |
| Works from on-prem | No | Yes, over VPN/ExpressRoute with DNS forwarding |
| Cost | Free | Per endpoint per hour, plus data |
| Use when | Cost matters more than instance-level isolation, all access is from inside the VNet | Anything holding production data; anything reachable from on-prem |

Service endpoints also change the source address the service sees, which breaks IP-based allow lists.

## Outbound Connectivity and SNAT

- **Default outbound access is being retired**: new subnets do not get implicit internet egress, so a VM with no public IP, no NAT Gateway and no load-balancer outbound rule simply cannot reach the internet. Every new subnet needs an explicit outbound method chosen at design time.
- **NAT Gateway is the default answer**: a large pool of SNAT ports per attached public IP, dynamic allocation across the subnet, and a 4-minute idle timeout that can be raised. It fixes exhaustion problems that outbound rules only postpone.
- **Load-balancer SNAT gives 1,024 ports per instance by default**, statically pre-allocated. A chatty service opening many short-lived connections to one destination exhausts that ceiling and produces the classic symptom: everything works, then intermittent connection timeouts under load, with no error in the application.
- Diagnosis: `SNATConnectionCount` and `AllocatedSnatPorts` metrics, plus the observation that failures correlate with request volume rather than with a specific destination.
- Mitigations in order: NAT Gateway; connection pooling and keep-alive in the application (the actual root cause most of the time); private endpoints for Azure destinations, which use no SNAT ports at all; more frontend IPs last.
- Assigning a public IP directly to a VM gives it its own SNAT and bypasses this — at the cost of an internet-exposed NIC. Rarely the right trade.

## Peering, Hubs and Routing

- **Peering is non-transitive.** A spoke peered to a hub cannot reach another spoke through it unless something routes: user-defined routes pointing at a firewall or NVA, Azure Route Server, or Virtual WAN.
- Peering bills on both sides for traffic that crosses it. A chatty hub-and-spoke pays per hop, in both directions.
- **Gateway transit** lets spokes use the hub's VPN/ExpressRoute gateway — enable it on both sides of the peering, or on-prem routes never appear in the spokes.
- User-defined routes override system routes; the most specific prefix wins, and `0.0.0.0/0` to a firewall forces all egress through it — including traffic to Azure services, which then needs the firewall to allow it.
- Deleting an NVA without removing its routes leaves a black hole that looks exactly like an NSG problem. Check effective routes before effective rules when the symptom is a timeout with no reset.
- **Virtual WAN** replaces hand-built hubs when the estate has many regions or many branch sites; it is a different cost and operating model, not a drop-in upgrade.

## Load Balancing Front Doors

| Product | Layer | Scope | Use when |
|---|---|---|---|
| Load Balancer | L4 | Regional | TCP/UDP, internal load balancing, high throughput, no HTTP awareness needed |
| Application Gateway | L7 | Regional | Path/host routing, WAF, TLS termination close to the backend, private backends |
| Front Door | L7 | Global anycast | Global entry, edge caching, WAF at the edge, fast multi-region failover |
| Traffic Manager | DNS | Global | Failover between endpoints that are not HTTP, or across products; DNS TTL bounds failover speed |

- Front Door and Traffic Manager fail over at different speeds: anycast withdrawal is near-immediate, DNS is bounded by the record TTL plus resolver behaviour. Never quote a DNS-based RTO shorter than the TTL.
- Application Gateway 502s are usually the backend health probe failing or a host-name mismatch: if the backend expects a specific `Host` header, the HTTP setting must send it (`pickHostNameFromBackendAddress`, or an explicit override).
- Health probes originate from the platform, not from your VNet — allow `AzureLoadBalancer` inbound, and make the probe path cheap, unauthenticated, and honest about dependencies.
- Layering Front Door in front of Application Gateway is a legitimate pattern (global edge + regional WAF), but lock the gateway to Front Door's service tag and header, or the origin is publicly reachable and the WAF is optional.

## Hybrid Connectivity

- **VPN Gateway** — site-to-site over the internet, hourly cost, throughput bounded by SKU. Correct for branch offices and for backup paths.
- **ExpressRoute** — private circuit through a partner: predictable latency, higher cost, long lead time. The circuit's SLA covers the circuit, not your gateway; zone-redundant gateway SKUs exist for a reason.
- Route advertisement is the thing that breaks: BGP sessions up but no prefixes, or on-prem advertising a supernet that swallows Azure's own ranges.
- Overlapping address space between on-prem and Azure is fatal and common after an acquisition — it is why the address plan is an artifact and not a memory.

## DNS Inside a VNet

- Default: Azure-provided DNS at 168.63.129.16, which resolves public names plus linked private zones and instance names.
- Custom DNS on the VNet applies to every resource in it, and every private zone then depends on those servers forwarding correctly.
- **Azure DNS Private Resolver** replaces the pair of DNS-forwarder VMs everyone used to run: inbound endpoints for on-prem queries, outbound endpoints plus forwarding rulesets for on-prem zones.
- Public DNS zones for a domain the user owns belong in the shared box: write the zone, its registrar-facing nameservers, and anything you bound to it into `~/Clawic/data/domains/domains.md`, with certificate expiry mirrored into `## Due` (`memory-template.md`).
