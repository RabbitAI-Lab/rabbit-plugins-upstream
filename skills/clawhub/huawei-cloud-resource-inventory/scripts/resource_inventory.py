#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Query all Huawei Cloud resources under a tenant and display their relationships
in grouped tables.

This is a read-only aggregation skill. It queries multiple Huawei Cloud services
(ECS / BMS / RDS / EVS / DCS / CCE / VPC / EIP / ELB / NAT / DNS) across all
regions, builds an in-memory relationship index, and outputs results as
plain-text tables grouped by resource type.

Usage:
  python3 resource_inventory.py [--region cn-north-4]
                                 [--resource-type ecs,bms,rds,evs,dcs,cce,vpc,eip,elb,nat,dns]
                                 [--format table|json]
                                 [--capability-list]

Examples:
  python3 resource_inventory.py
  python3 resource_inventory.py --region cn-north-4
  python3 resource_inventory.py --resource-type ecs,vpc,eip
  python3 resource_inventory.py --format json
"""

import argparse
import json
import os
import sys
import traceback

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_REGIONS = [
    "cn-north-1", "cn-north-4", "cn-north-9", "cn-north-12",
    "cn-east-3", "cn-south-1", "cn-southwest-2",
    "ap-southeast-1", "ap-southeast-2", "ap-southeast-3",
    "af-south-1", "la-south-2",
]

ALL_RESOURCE_TYPES = [
    "ecs", "bms", "rds", "evs", "dcs", "cce",
    "vpc", "subnet", "eip", "elb", "nat", "dns",
]


def _load_credentials():
    """Dynamically scan environment variables for AK/SK.

    Scans HUAWEI / HW / HWC / OBS prefixed variables containing
    ACCESS_KEY / _AK / SECRET_KEY / _SK patterns.
    """
    ak, sk = "", ""
    for k, v in os.environ.items():
        u = k.upper()
        if not (u.startswith("HUAWEI") or u.startswith("HW")
                or u.startswith("HWC") or u.startswith("OBS")):
            continue
        if "ACCESS_KEY" in u or u.endswith("_AK") or u == "AK":
            if v:
                ak = v
        if "SECRET_KEY" in u or u.endswith("_SK") or u == "SK":
            if v:
                sk = v
    return ak, sk


def _get_http_config():
    """Build HTTP config with proxy and timeout settings."""
    from huaweicloudsdkcore.http.http_config import HttpConfig
    from urllib.parse import urlparse

    http_config = HttpConfig.get_default_config()
    http_config.ignore_ssl_verification = True
    http_config.timeout = 30
    http_config.retry_times = 3

    proxy_url = os.getenv("HTTPS_PROXY", "") or os.getenv("HTTP_PROXY", "")
    if proxy_url:
        parsed = urlparse(proxy_url)
        http_config.proxy_protocol = parsed.scheme or "http"
        http_config.proxy_host = parsed.hostname or ""
        http_config.proxy_port = parsed.port or 8080
        http_config.proxy_user = parsed.username or ""
        http_config.proxy_password = parsed.password or ""

    return http_config


def _build_credentials(ak, sk):
    """Build BasicCredentials from AK/SK."""
    from huaweicloudsdkcore.auth.credentials import BasicCredentials
    return BasicCredentials(ak, sk)


def _safe_getattr(obj, name, default=""):
    """Safely get an attribute, returning default if not present."""
    val = getattr(obj, name, default)
    if val is None:
        return default
    return val


def _fmt_val(val, max_len=40):
    """Format a value for table display, truncating if needed."""
    if val is None:
        return "-"
    s = str(val)
    if len(s) > max_len:
        return s[:max_len - 3] + "..."
    return s


class ResourceInventory:
    """Aggregates cloud resources across regions and builds relationships."""

    def __init__(self, ak, sk, regions=None):
        self.ak = ak
        self.sk = sk
        self.regions = regions or DEFAULT_REGIONS
        self.http_config = _get_http_config()
        self.credentials = _build_credentials(ak, sk)

        self.resources = {}
        self.errors = []

        self.vpc_index = {}
        self.subnet_index = {}
        self.eip_port_index = {}
        self.evs_server_index = {}
        self.ecs_id_index = {}
        self.cce_cluster_index = {}

    def _build_client(self, client_cls, region_cls, region):
        """Build an SDK client for a given region.

        Returns ``None`` (and records an error) when the SDK does not support the
        given region for this service, so a single unsupported region does not
        abort the whole inventory query.
        """
        try:
            region_obj = region_cls.value_of(region)
        except Exception as e:
            err_msg = f"{client_cls.__name__} in {region}: region not supported: {type(e).__name__}: {_fmt_val(str(e), 120)}"
            self.errors.append(err_msg)
            return None
        return client_cls.new_builder() \
            .with_http_config(self.http_config) \
            .with_credentials(self.credentials) \
            .with_region(region_obj) \
            .build()

    def _safe_query(self, service, region, query_fn):
        """Wrap a query call with error handling."""
        try:
            return query_fn()
        except Exception as e:
            err_msg = f"{service} in {region}: {type(e).__name__}: {_fmt_val(str(e), 120)}"
            self.errors.append(err_msg)
            return None

    def query_ecs(self, region):
        """Query ECS instances (cloud servers)."""
        from huaweicloudsdkecs.v2.ecs_client import EcsClient
        from huaweicloudsdkecs.v2.model import ListServersDetailsRequest
        from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion

        client = self._build_client(EcsClient, EcsRegion, region)
        if client is None:
            return []
        all_servers = []
        offset = 1
        while True:
            req = ListServersDetailsRequest(limit=100, offset=offset)
            resp = self._safe_query("ECS", region, lambda: client.list_servers_details(req))
            if resp is None:
                break
            servers = resp.servers or []
            if not servers:
                break
            all_servers.extend(servers)
            total = getattr(resp, "count", 0) or 0
            if total and len(all_servers) >= total:
                break
            if len(servers) < 100:
                break
            offset += 1

        results = []
        for s in all_servers:
            vpc_id = _safe_getattr(s, "metadata", {}).get("vpc_id", "") if isinstance(_safe_getattr(s, "metadata", {}), dict) else ""
            subnet_ids = []
            private_ips = []
            public_ips = []
            port_ids = []

            ni_list = _safe_getattr(s, "network_interfaces", [])
            if isinstance(ni_list, list):
                for ni in ni_list:
                    if isinstance(ni, dict):
                        sid = ni.get("subnet_id", "")
                        if sid:
                            subnet_ids.append(sid)
                        ips = ni.get("ip_addresses", [])
                        if isinstance(ips, list):
                            private_ips.extend(ips)
                        port_id = ni.get("port_id", "")
                        if port_id:
                            port_ids.append(port_id)
                        assoc = ni.get("association")
                        if isinstance(assoc, dict) and assoc.get("public_ip_address"):
                            public_ips.append(assoc["public_ip_address"])
                    else:
                        sid = _safe_getattr(ni, "subnet_id")
                        if sid:
                            subnet_ids.append(sid)
                        port_id = _safe_getattr(ni, "port_id")
                        if port_id:
                            port_ids.append(port_id)
                        ip_list = _safe_getattr(ni, "ip_addresses", [])
                        if isinstance(ip_list, list):
                            private_ips.extend(ip_list)
                        assoc = _safe_getattr(ni, "association")
                        if isinstance(assoc, dict):
                            pub_ip = assoc.get("public_ip_address", "")
                        else:
                            pub_ip = _safe_getattr(assoc, "public_ip_address")
                        if pub_ip:
                            public_ips.append(pub_ip)

            if not vpc_id:
                vpc_id = _safe_getattr(s, "vpc_id", "")

            volume_ids = []
            vol_attr = _safe_getattr(s, "os_extended_volumesvolumes_attached", [])
            if isinstance(vol_attr, list):
                for v in vol_attr:
                    if isinstance(v, dict):
                        vid = v.get("id", "")
                    else:
                        vid = _safe_getattr(v, "id")
                    if vid:
                        volume_ids.append(vid)

            flavor_info = _safe_getattr(s, "flavor")
            if isinstance(flavor_info, dict):
                flavor_name = flavor_info.get("name", "")
            else:
                flavor_name = _safe_getattr(flavor_info, "name")

            server_id = _safe_getattr(s, "id")
            entry = {
                "id": server_id,
                "name": _safe_getattr(s, "name"),
                "status": _safe_getattr(s, "status"),
                "flavor": flavor_name,
                "vpc_id": vpc_id,
                "subnet_ids": ",".join(subnet_ids),
                "private_ips": ",".join(private_ips) if private_ips else "-",
                "public_ips": ",".join(public_ips) if public_ips else "-",
                "eip_port_ids": ",".join(port_ids),
                "volume_ids": ",".join(volume_ids),
                "az": _safe_getattr(s, "os_ext_a_zavailability_zone"),
                "enterprise_project_id": _safe_getattr(s, "enterprise_project_id"),
                "region": region,
            }
            results.append(entry)
            self.ecs_id_index[server_id] = entry
            for pid in port_ids:
                self.eip_port_index[pid] = server_id
            for vid in volume_ids:
                self.evs_server_index[vid] = server_id

        return results

    def query_bms(self, region):
        """Query BMS (bare metal servers)."""
        from huaweicloudsdkbms.v1.bms_client import BmsClient
        from huaweicloudsdkbms.v1.model import ListBareMetalServersDetailRequest
        from huaweicloudsdkbms.v1.region.bms_region import BmsRegion

        client = self._build_client(BmsClient, BmsRegion, region)
        if client is None:
            return []
        all_servers = []
        offset = 1
        while True:
            req = ListBareMetalServersDetailRequest(limit=100, offset=offset)
            resp = self._safe_query("BMS", region, lambda: client.list_bare_metal_servers_detail(req))
            if resp is None:
                break
            servers = resp.servers or []
            if not servers:
                break
            all_servers.extend(servers)
            if len(servers) < 100:
                break
            offset += 1

        results = []
        for s in all_servers:
            entry = {
                "id": _safe_getattr(s, "id"),
                "name": _safe_getattr(s, "name"),
                "status": _safe_getattr(s, "status"),
                "flavor": _safe_getattr(s, "flavor", {}).get("id", "") if isinstance(_safe_getattr(s, "flavor"), dict) else str(_safe_getattr(s, "flavor")),
                "vpc_id": "-",
                "subnet_ids": "-",
                "private_ips": "-",
                "public_ips": "-",
                "az": _safe_getattr(s, "os_ext_a_zavailability_zone"),
                "region": region,
            }
            results.append(entry)
        return results

    def query_rds(self, region):
        """Query RDS instances."""
        from huaweicloudsdkrds.v3.rds_client import RdsClient
        from huaweicloudsdkrds.v3.model import ListInstancesRequest
        from huaweicloudsdkrds.v3.region.rds_region import RdsRegion

        client = self._build_client(RdsClient, RdsRegion, region)
        if client is None:
            return []
        all_instances = []
        offset = 0
        while True:
            req = ListInstancesRequest(limit=100, offset=offset)
            resp = self._safe_query("RDS", region, lambda: client.list_instances(req))
            if resp is None:
                break
            instances = resp.instances or []
            if not instances:
                break
            all_instances.extend(instances)
            total = getattr(resp, "total_count", 0)
            offset += len(instances)
            if offset >= total or len(instances) < 100:
                break

        results = []
        for i in all_instances:
            datastore = _safe_getattr(i, "datastore", {})
            if isinstance(datastore, dict):
                engine = datastore.get("type", "")
                version = datastore.get("version", "")
            else:
                engine = _safe_getattr(datastore, "type")
                version = _safe_getattr(datastore, "version")

            entry = {
                "id": _safe_getattr(i, "id"),
                "name": _safe_getattr(i, "name"),
                "status": _safe_getattr(i, "status"),
                "engine": engine,
                "version": version,
                "flavor": _safe_getattr(i, "flavor_ref"),
                "vpc_id": _safe_getattr(i, "vpc_id"),
                "subnet_id": _safe_getattr(i, "subnet_id"),
                "private_ips": ",".join(_safe_getattr(i, "private_ips", [])) if isinstance(_safe_getattr(i, "private_ips"), list) else str(_safe_getattr(i, "private_ips")),
                "type": _safe_getattr(i, "type"),
                "region": region,
            }
            results.append(entry)
        return results

    def query_evs(self, region):
        """Query EVS (cloud volumes)."""
        from huaweicloudsdkevs.v2.evs_client import EvsClient
        from huaweicloudsdkevs.v2.model import ListVolumesRequest
        from huaweicloudsdkevs.v2.region.evs_region import EvsRegion

        client = self._build_client(EvsClient, EvsRegion, region)
        if client is None:
            return []
        all_volumes = []
        offset = 0
        while True:
            req = ListVolumesRequest(limit=100, offset=offset)
            resp = self._safe_query("EVS", region, lambda: client.list_volumes(req))
            if resp is None:
                break
            volumes = resp.volumes or []
            if not volumes:
                break
            all_volumes.extend(volumes)
            total = getattr(resp, "count", 0)
            offset += len(volumes)
            if total and offset >= total:
                break
            if len(volumes) < 100:
                break

        results = []
        for v in all_volumes:
            attached_servers = []
            for a in (_safe_getattr(v, "attachments", []) or []):
                if isinstance(a, dict):
                    attached_servers.append(a.get("server_id", ""))
                else:
                    sid = _safe_getattr(a, "server_id")
                    if sid:
                        attached_servers.append(sid)

            entry = {
                "id": _safe_getattr(v, "id"),
                "name": _safe_getattr(v, "name"),
                "status": _safe_getattr(v, "status"),
                "size": str(_safe_getattr(v, "size", "")),
                "type": _safe_getattr(v, "volume_type"),
                "az": _safe_getattr(v, "availability_zone"),
                "attached_to": ",".join(attached_servers) if attached_servers else "-",
                "bootable": _safe_getattr(v, "bootable"),
                "region": region,
            }
            results.append(entry)
        return results

    def query_dcs(self, region):
        """Query DCS (distributed cache service) instances."""
        from huaweicloudsdkdcs.v2.dcs_client import DcsClient
        from huaweicloudsdkdcs.v2.model import ListInstancesRequest
        from huaweicloudsdkdcs.v2.region.dcs_region import DcsRegion

        client = self._build_client(DcsClient, DcsRegion, region)
        if client is None:
            return []
        all_instances = []
        offset = 0
        while True:
            req = ListInstancesRequest(limit=100, offset=offset)
            resp = self._safe_query("DCS", region, lambda: client.list_instances(req))
            if resp is None:
                break
            instances = resp.instances or []
            if not instances:
                break
            all_instances.extend(instances)
            total = getattr(resp, "instance_num", 0) or 0
            offset += len(instances)
            if total and offset >= total:
                break
            if len(instances) < 100:
                break

        results = []
        for i in all_instances:
            entry = {
                "id": _safe_getattr(i, "instance_id"),
                "name": _safe_getattr(i, "name"),
                "status": _safe_getattr(i, "status"),
                "engine": _safe_getattr(i, "engine"),
                "capacity": str(_safe_getattr(i, "capacity")),
                "vpc_id": _safe_getattr(i, "vpc_id"),
                "subnet_id": _safe_getattr(i, "subnet_id"),
                "available_zones": ",".join(_safe_getattr(i, "available_zones", []) or []),
                "region": region,
            }
            results.append(entry)
        return results

    def query_cce(self, region):
        """Query CCE clusters and nodes."""
        from huaweicloudsdkcce.v3.cce_client import CceClient
        from huaweicloudsdkcce.v3.model import ListClustersRequest, ListNodesRequest
        from huaweicloudsdkcce.v3.region.cce_region import CceRegion

        client = self._build_client(CceClient, CceRegion, region)
        if client is None:
            return []
        req = ListClustersRequest(detail=True)
        resp = self._safe_query("CCE", region, lambda: client.list_clusters(req))
        if resp is None:
            return []

        results = []
        for cl in (resp.items or []):
            md = cl.metadata if cl.metadata else None
            sp = cl.spec if cl.spec else None
            cluster_id = _safe_getattr(md, "uid") if md else ""
            cluster_name = _safe_getattr(md, "name") if md else ""

            vpc_id = ""
            subnet_id = ""
            if sp and sp.host_network:
                vpc_id = _safe_getattr(sp.host_network, "vpc")
                subnet_id = _safe_getattr(sp.host_network, "subnet")

            container_vpc_id = ""
            container_subnet_id = ""
            if sp and sp.container_network:
                container_vpc_id = _safe_getattr(sp.container_network, "vpc")
                container_subnet_id = _safe_getattr(sp.container_network, "subnet")

            node_count = 0
            node_names = []
            if cluster_id:
                try:
                    marker = None
                    while True:
                        nr_req = ListNodesRequest(cluster_id=cluster_id, limit=200, marker=marker)
                        nr = client.list_nodes(nr_req)
                        nodes = nr.items or []
                        node_count += len(nodes)
                        for n in nodes:
                            nmd = n.metadata if n.metadata else None
                            if nmd:
                                node_names.append(_safe_getattr(nmd, "name"))
                        page_info = getattr(nr, "page_info", None)
                        next_marker = getattr(page_info, "next_marker", None) if page_info else None
                        if not next_marker or not nodes:
                            break
                        marker = next_marker
                except Exception as e:
                    self.errors.append(f"CCE nodes in {region}: {_fmt_val(str(e), 80)}")

            entry = {
                "id": cluster_id,
                "name": cluster_name,
                "status": _safe_getattr(cl.status, "phase") if cl.status else "",
                "vpc_id": vpc_id,
                "subnet_id": subnet_id,
                "container_network_vpc_id": container_vpc_id,
                "node_count": str(node_count),
                "nodes": ",".join(node_names[:5]) + ("..." if len(node_names) > 5 else "") if node_names else "-",
                "version": _safe_getattr(sp, "version") if sp else "",
                "region": region,
            }
            results.append(entry)
            self.cce_cluster_index[cluster_id] = entry
        return results

    def query_vpc(self, region):
        """Query VPCs."""
        from huaweicloudsdkvpc.v3.vpc_client import VpcClient
        from huaweicloudsdkvpc.v3.model import ListVpcsRequest
        from huaweicloudsdkvpc.v3.region.vpc_region import VpcRegion

        client = self._build_client(VpcClient, VpcRegion, region)
        if client is None:
            return []
        all_vpcs = []
        marker = None
        while True:
            req = ListVpcsRequest(limit=100)
            if marker:
                req.marker = marker
            resp = self._safe_query("VPC", region, lambda: client.list_vpcs(req))
            if resp is None:
                break
            vpcs = resp.vpcs or []
            if not vpcs:
                break
            all_vpcs.extend(vpcs)
            page_info = getattr(resp, "page_info", None)
            next_marker = getattr(page_info, "next_marker", None) if page_info else None
            if not next_marker:
                break
            marker = next_marker

        results = []
        for v in all_vpcs:
            vid = _safe_getattr(v, "id")
            entry = {
                "id": vid,
                "name": _safe_getattr(v, "name"),
                "cidr": _safe_getattr(v, "cidr"),
                "status": _safe_getattr(v, "status"),
                "description": _safe_getattr(v, "description"),
                "enterprise_project_id": _safe_getattr(v, "enterprise_project_id"),
                "region": region,
            }
            results.append(entry)
            self.vpc_index[vid] = entry
        return results

    def query_subnet(self, region):
        """Query subnets (VPC v2 API)."""
        from huaweicloudsdkvpc.v2.vpc_client import VpcClient as VpcClientV2
        from huaweicloudsdkvpc.v2.model import ListSubnetsRequest
        from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion as VpcRegionV2

        client = self._build_client(VpcClientV2, VpcRegionV2, region)
        if client is None:
            return []
        all_subnets = []
        marker = None
        while True:
            req = ListSubnetsRequest(limit=100)
            if marker:
                req.marker = marker
            resp = self._safe_query("Subnet", region, lambda: client.list_subnets(req))
            if resp is None:
                break
            subnets = resp.subnets or []
            if not subnets:
                break
            all_subnets.extend(subnets)
            page_info = getattr(resp, "page_info", None)
            next_marker = getattr(page_info, "next_marker", None) if page_info else None
            if not next_marker:
                break
            marker = next_marker

        results = []
        for s in all_subnets:
            sid = _safe_getattr(s, "id")
            vpc_id = _safe_getattr(s, "vpc_id")
            entry = {
                "id": sid,
                "name": _safe_getattr(s, "name"),
                "cidr": _safe_getattr(s, "cidr"),
                "vpc_id": vpc_id,
                "vpc_name": self.vpc_index.get(vpc_id, {}).get("name", "-"),
                "status": _safe_getattr(s, "status"),
                "az": _safe_getattr(s, "availability_zone"),
                "region": region,
            }
            results.append(entry)
            self.subnet_index[sid] = entry
        return results

    def query_eip(self, region):
        """Query EIPs (elastic public IPs)."""
        from huaweicloudsdkeip.v2.eip_client import EipClient
        from huaweicloudsdkeip.v2.model import ListPublicipsRequest
        from huaweicloudsdkeip.v2.region.eip_region import EipRegion

        client = self._build_client(EipClient, EipRegion, region)
        if client is None:
            return []
        all_eips = []
        marker = None
        while True:
            req = ListPublicipsRequest(limit=100)
            if marker:
                req.marker = marker
            resp = self._safe_query("EIP", region, lambda: client.list_publicips(req))
            if resp is None:
                break
            eips = resp.publicips or []
            if not eips:
                break
            all_eips.extend(eips)
            page_info = getattr(resp, "page_info", None)
            next_marker = getattr(page_info, "next_marker", None) if page_info else None
            if not next_marker:
                break
            marker = next_marker

        results = []
        for p in all_eips:
            port_id = _safe_getattr(p, "port_id")
            associated_server = self.eip_port_index.get(port_id, "-")

            entry = {
                "id": _safe_getattr(p, "id"),
                "public_ip": _safe_getattr(p, "public_ip_address"),
                "private_ip": _safe_getattr(p, "ip_address"),
                "type": _safe_getattr(p, "type"),
                "status": _safe_getattr(p, "status"),
                "port_id": port_id,
                "associated_server": associated_server,
                "enterprise_project_id": _safe_getattr(p, "enterprise_project_id"),
                "region": region,
            }
            results.append(entry)
        return results

    def query_elb(self, region):
        """Query ELB (elastic load balancers)."""
        from huaweicloudsdkelb.v3.elb_client import ElbClient
        from huaweicloudsdkelb.v3.model import ListLoadBalancersRequest
        from huaweicloudsdkelb.v3.region.elb_region import ElbRegion

        client = self._build_client(ElbClient, ElbRegion, region)
        if client is None:
            return []

        all_lbs = []
        marker = None
        while True:
            req = ListLoadBalancersRequest(limit=100)
            if marker:
                req.marker = marker
            resp = self._safe_query("ELB", region, lambda: client.list_load_balancers(req))
            if resp is None:
                break
            lbs = resp.loadbalancers or []
            if not lbs:
                break
            all_lbs.extend(lbs)
            page_info = getattr(resp, "page_info", None)
            next_marker = getattr(page_info, "next_marker", None) if page_info else None
            if not next_marker:
                break
            marker = next_marker

        results = []
        for lb in all_lbs:
            vpc_id = _safe_getattr(lb, "vpc_id")
            subnet_id = _safe_getattr(lb, "vip_subnet_cidr_id")
            entry = {
                "id": _safe_getattr(lb, "id"),
                "name": _safe_getattr(lb, "name"),
                "status": _safe_getattr(lb, "provisioning_status"),
                "operating_status": _safe_getattr(lb, "operating_status"),
                "vpc_id": vpc_id,
                "vpc_name": self.vpc_index.get(vpc_id, {}).get("name", "-"),
                "subnet_id": subnet_id,
                "vip_address": _safe_getattr(lb, "vip_address"),
                "provider": _safe_getattr(lb, "provider"),
                "region": region,
            }
            results.append(entry)
        return results

    def query_nat(self, region):
        """Query NAT gateways."""
        from huaweicloudsdknat.v2.nat_client import NatClient
        from huaweicloudsdknat.v2.model import ListNatGatewaysRequest
        from huaweicloudsdknat.v2.region.nat_region import NatRegion

        client = self._build_client(NatClient, NatRegion, region)
        if client is None:
            return []

        all_gws = []
        marker = None
        while True:
            req = ListNatGatewaysRequest(limit=200)
            if marker:
                req.marker = marker
            resp = self._safe_query("NAT", region, lambda: client.list_nat_gateways(req))
            if resp is None:
                break
            gws = resp.nat_gateways or []
            if not gws:
                break
            all_gws.extend(gws)
            if len(gws) < 200:
                break
            marker = _safe_getattr(gws[-1], "id")

        results = []
        for n in all_gws:
            router_id = _safe_getattr(n, "router_id")
            entry = {
                "id": _safe_getattr(n, "id"),
                "name": _safe_getattr(n, "name"),
                "status": _safe_getattr(n, "status"),
                "vpc_id": router_id,
                "vpc_name": self.vpc_index.get(router_id, {}).get("name", "-"),
                "internal_network_id": _safe_getattr(n, "internal_network_id"),
                "spec": _safe_getattr(n, "spec"),
                "enterprise_project_id": _safe_getattr(n, "enterprise_project_id"),
                "region": region,
            }
            results.append(entry)
        return results

    def query_dns(self, region):
        """Query DNS zones (public + private)."""
        from huaweicloudsdkdns.v2.dns_client import DnsClient
        from huaweicloudsdkdns.v2.model import ListPublicZonesRequest, ListPrivateZonesRequest
        from huaweicloudsdkdns.v2.region.dns_region import DnsRegion

        client = self._build_client(DnsClient, DnsRegion, region)
        if client is None:
            return []
        results = []
        seen_ids = set()

        def _append_zones(zones, default_type):
            for z in (zones or []):
                zid = _safe_getattr(z, "id")
                if not zid or zid in seen_ids:
                    continue
                seen_ids.add(zid)
                ztype = _safe_getattr(z, "zone_type") or default_type
                entry = {
                    "id": zid,
                    "name": _safe_getattr(z, "name"),
                    "zone_type": ztype,
                    "status": _safe_getattr(z, "status"),
                    "record_num": str(_safe_getattr(z, "record_num")),
                    "region": region,
                }
                results.append(entry)

        marker = None
        while True:
            req_pub = ListPublicZonesRequest(limit=100)
            if marker:
                req_pub.marker = marker
            resp_pub = self._safe_query("DNS-Public", region, lambda: client.list_public_zones(req_pub))
            if resp_pub is None:
                break
            _append_zones(resp_pub.zones, "public")
            pub_meta = getattr(resp_pub, "metadata", None)
            next_marker = getattr(pub_meta, "next_marker", None) if pub_meta else None
            if not next_marker:
                break
            marker = next_marker

        marker = None
        while True:
            req_pri = ListPrivateZonesRequest(limit=100)
            if marker:
                req_pri.marker = marker
            resp_pri = self._safe_query("DNS-Private", region, lambda: client.list_private_zones(req_pri))
            if resp_pri is None:
                break
            _append_zones(resp_pri.zones, "private")
            pri_meta = getattr(resp_pri, "metadata", None)
            next_marker = getattr(pri_meta, "next_marker", None) if pri_meta else None
            if not next_marker:
                break
            marker = next_marker
        return results

    def run(self, resource_types):
        """Execute queries for all specified resource types across all regions."""
        query_map = {
            "vpc": self.query_vpc,
            "subnet": self.query_subnet,
            "ecs": self.query_ecs,
            "bms": self.query_bms,
            "eip": self.query_eip,
            "elb": self.query_elb,
            "nat": self.query_nat,
            "rds": self.query_rds,
            "evs": self.query_evs,
            "dcs": self.query_dcs,
            "cce": self.query_cce,
            "dns": self.query_dns,
        }

        ordered_types = [t for t in ALL_RESOURCE_TYPES if t in resource_types]

        for rt in ordered_types:
            fn = query_map.get(rt)
            if not fn:
                continue
            self.resources[rt] = []
            for region in self.regions:
                items = fn(region)
                if items:
                    self.resources[rt].extend(items)

    def render_table(self, title, columns, rows):
        """Render a plain-text table."""
        if not rows:
            return f"\n## {title}\n\n(no resources found)\n"

        col_widths = [len(c) for c in columns]
        for row in rows:
            for i, col in enumerate(columns):
                val = str(row.get(col, "-"))
                if len(val) + 2 > col_widths[i]:
                    col_widths[i] = len(val) + 2

        separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
        header = "|" + "|".join(f" {c:<{w}} " for c, w in zip(columns, col_widths)) + "|"

        lines = [f"\n## {title} ({len(rows)} total)\n"]
        lines.append("```")
        lines.append(separator)
        lines.append(header)
        lines.append(separator)
        for row in rows:
            cells = []
            for i, col in enumerate(columns):
                val = str(row.get(col, "-"))
                cells.append(f" {val:<{col_widths[i]}} ")
            lines.append("|" + "|".join(cells) + "|")
        lines.append(separator)
        lines.append("```")
        return "\n".join(lines)

    def render(self):
        """Render all resource tables."""
        output_parts = []

        table_configs = [
            ("VPC", ["id", "name", "cidr", "status", "enterprise_project_id", "region"], "vpc"),
            ("Subnet", ["id", "name", "cidr", "vpc_id", "vpc_name", "az", "status", "region"], "subnet"),
            ("ECS (Cloud Servers)", ["id", "name", "status", "flavor", "vpc_id", "subnet_ids", "private_ips", "public_ips", "volume_ids", "az", "region"], "ecs"),
            ("BMS (Bare Metal Servers)", ["id", "name", "status", "flavor", "az", "region"], "bms"),
            ("EIP (Elastic Public IP)", ["id", "public_ip", "private_ip", "type", "status", "port_id", "associated_server", "region"], "eip"),
            ("ELB (Load Balancers)", ["id", "name", "status", "vpc_id", "vpc_name", "subnet_id", "vip_address", "provider", "region"], "elb"),
            ("NAT (NAT Gateways)", ["id", "name", "status", "vpc_id", "vpc_name", "internal_network_id", "spec", "region"], "nat"),
            ("RDS (Relational Database)", ["id", "name", "status", "engine", "version", "flavor", "vpc_id", "subnet_id", "private_ips", "type", "region"], "rds"),
            ("EVS (Cloud Volumes)", ["id", "name", "status", "size", "type", "az", "attached_to", "bootable", "region"], "evs"),
            ("DCS (Distributed Cache)", ["id", "name", "status", "engine", "capacity", "vpc_id", "subnet_id", "available_zones", "region"], "dcs"),
            ("CCE (Container Clusters)", ["id", "name", "status", "vpc_id", "subnet_id", "node_count", "nodes", "version", "region"], "cce"),
            ("DNS (Zones)", ["id", "name", "zone_type", "status", "record_num", "region"], "dns"),
        ]

        for title, columns, key in table_configs:
            rows = self.resources.get(key, [])
            output_parts.append(self.render_table(title, columns, rows))

        if self.errors:
            output_parts.append("\n## Query Errors / Warnings\n")
            output_parts.append("```")
            for err in self.errors:
                output_parts.append(f"  - {err}")
            output_parts.append("```\n")

        total = sum(len(v) for v in self.resources.values())
        output_parts.append(f"\n## Summary\n")
        output_parts.append(f"Total resources found: {total}")
        for key in ALL_RESOURCE_TYPES:
            count = len(self.resources.get(key, []))
            if count > 0:
                output_parts.append(f"  - {key.upper()}: {count}")

        return "\n".join(output_parts)

    def render_json(self):
        """Render all resources as JSON."""
        return json.dumps(self.resources, ensure_ascii=False, indent=2)


def capability_list():
    """Print the list of supported capabilities."""
    print("Supported resource types:")
    for rt in ALL_RESOURCE_TYPES:
        print(f"  - {rt}")
    print(f"\nSupported regions: {', '.join(DEFAULT_REGIONS)}")
    print("\nOutput formats: table (default), json")
    print("\nUsage examples:")
    print("  python3 resource_inventory.py                          # Query all resources in all regions")
    print("  python3 resource_inventory.py --region cn-north-4       # Query a specific region")
    print("  python3 resource_inventory.py --resource-type ecs,vpc   # Query specific resource types")
    print("  python3 resource_inventory.py --format json             # Output as JSON")


def main():
    parser = argparse.ArgumentParser(
        description="Query all Huawei Cloud resources under a tenant and display relationships in tables."
    )
    parser.add_argument("--region", type=str, default=None,
                        help="Specific region (default: all regions)")
    parser.add_argument("--resource-type", type=str, default=None,
                        help=f"Comma-separated resource types (default: all). Options: {','.join(ALL_RESOURCE_TYPES)}")
    parser.add_argument("--format", choices=["table", "json"], default="table",
                        help="Output format (default: table)")
    parser.add_argument("--capability-list", action="store_true",
                        help="List supported resource types and exit")
    args = parser.parse_args()

    if args.capability_list:
        capability_list()
        return

    ak, sk = _load_credentials()
    if not ak or not sk:
        print("ERROR: AK/SK not found in environment variables.")
        print("Set one of: HUAWEICLOUD_SDK_AK/SK, HW_ACCESS_KEY/SECRET_KEY, OBS_ACCESS_KEY/SECRET_KEY")
        sys.exit(3)

    regions = DEFAULT_REGIONS
    if args.region:
        requested_regions = [r.strip() for r in args.region.split(",") if r.strip()]
        if not requested_regions:
            print("ERROR: --region must be a comma-separated list of region IDs.")
            sys.exit(1)
        regions = requested_regions

    resource_types = ALL_RESOURCE_TYPES
    if args.resource_type:
        requested = [t.strip().lower() for t in args.resource_type.split(",")]
        invalid = [t for t in requested if t not in ALL_RESOURCE_TYPES]
        if invalid:
            print(f"ERROR: Unknown resource type(s): {', '.join(invalid)}")
            print(f"Valid types: {', '.join(ALL_RESOURCE_TYPES)}")
            sys.exit(1)
        resource_types = requested

    print(f"Querying {len(resource_types)} resource type(s) across {len(regions)} region(s)...", file=sys.stderr)

    inventory = ResourceInventory(ak, sk, regions)
    inventory.run(resource_types)

    if args.format == "json":
        print(inventory.render_json())
    else:
        print(inventory.render())


if __name__ == "__main__":
    main()
