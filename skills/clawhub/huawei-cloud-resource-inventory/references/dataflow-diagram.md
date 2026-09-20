# 数据流图

## 请求/响应流程

```mermaid
graph TD
    A[User / Agent] --> B[resource_inventory.py]
    B --> C[Load AK/SK from env]
    C --> D[IAM: List Projects / Regions]
    D --> E{For each region}
    E --> F1[VPC v3: ListVpcs]
    E --> F2[VPC v2: ListSubnets]
    E --> F3[ECS v2: ListServersDetails]
    E --> F4[BMS v1: ListBareMetalServersDetail]
    E --> F5[EIP v2: ListPublicips]
    E --> F6[ELB v3: ListLoadBalancers]
    E --> F7[NAT v2: ListNatGateways]
    E --> F8[RDS v3: ListInstances]
    E --> F9[EVS v2: ListVolumes]
    E --> F10[DCS v2: ListInstances]
    E --> F11[CCE v3: ListClusters + ListNodes]
    E --> F12[DNS v2: ListPublicZones + ListPrivateZones]
    F1 --> G[Build Relationship Index]
    F2 --> G
    F3 --> G
    F5 --> G
    F8 --> G
    F9 --> G
    F11 --> G
    G --> H[VPC ↔ Subnet ↔ ECS]
    G --> I[EIP → ECS via port_id]
    G --> J[EVS → ECS via attachment]
    G --> K[CCE → VPC/Subnet]
    G --> L[ELB/NAT/RDS/DCS → VPC]
    H --> M[Render Grouped Tables]
    I --> M
    J --> M
    K --> M
    L --> M
    M --> N[Output: table / json]
```

## 关联索引构建

```text
1. vpc_index:     {vpc_id → vpc_entry}        (from VPC query)
2. subnet_index:  {subnet_id → subnet_entry}   (from Subnet query)
3. ecs_id_index:  {server_id → ecs_entry}      (from ECS query)
4. eip_port_index: {port_id → server_id}       (from ECS network_interfaces)
5. evs_server_index: {volume_id → server_id}   (from ECS volume attachments)

Cross-reference:
- EIP.associated_server = eip_port_index[EIP.port_id]
- EVS.attached_to = evs_server_index[EVS.id]  (or from EVS attachment directly)
- Subnet.vpc_name = vpc_index[Subnet.vpc_id].name
- ELB.vpc_name = vpc_index[ELB.vpc_id].name
- NAT.vpc_name = vpc_index[NAT.vpc_id].name
```
