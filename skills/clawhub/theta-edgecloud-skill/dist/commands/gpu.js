import { callThetaMcpTool } from '../clients/edgecloudMcp.js';
function withProject(projectId, args = {}) {
    const out = { project_id: projectId };
    for (const [key, value] of Object.entries(args))
        if (value !== undefined && value !== null && value !== '')
            out[key] = value;
    return out;
}
function requireConfirm(action, confirm) {
    if (confirm !== true) {
        throw new Error(`${action} changes billable GPU capacity. State the price, get explicit approval, then pass confirm:true.`);
    }
}
function filterResources(resources, filter) {
    const model = filter.gpuModel?.toLowerCase();
    const region = filter.region?.toLowerCase();
    const filtered = resources.filter((r) => (!filter.provider || r.provider === filter.provider)
        && (!model || String(r.gpu_model ?? '').toLowerCase().includes(model))
        && (!region || `${r.country ?? ''} ${r.region ?? ''}`.toLowerCase().includes(region))
        && (filter.maxPricePerHourUsd === undefined || (typeof r.price_per_hour_usd === 'number' && r.price_per_hour_usd <= filter.maxPricePerHourUsd))
        && (!filter.availableOnly || (r.gpu_count_available ?? 0) > 0));
    filtered.sort((a, b) => (a.price_per_hour_usd ?? Infinity) - (b.price_per_hour_usd ?? Infinity));
    return filter.limit ? filtered.slice(0, Math.max(1, Math.trunc(filter.limit))) : filtered;
}
function mutationPreview(tool, args) {
    return { dryRun: true, transport: 'theta-hosted-mcp', tool, arguments: args };
}
export const gpu = {
    listResources: async (cfg, projectId, filter = {}) => {
        const result = await callThetaMcpTool(cfg, 'list_gpu_resources', withProject(projectId));
        const all = Array.isArray(result?.resources) ? result.resources : [];
        const resources = filterResources(all, filter);
        return { ...result, totalResources: all.length, matchedResources: resources.length, resources, priceCurrency: 'USD per hour' };
    },
    getResource: (cfg, projectId, resourceId, region) => callThetaMcpTool(cfg, 'get_gpu_resource', withProject(projectId, { resource_id: resourceId, region })),
    listTemplates: (cfg, projectId) => callThetaMcpTool(cfg, 'list_gpu_deployment_templates', withProject(projectId)),
    listDeployments: (cfg, projectId) => callThetaMcpTool(cfg, 'list_gpu_deployments', withProject(projectId)),
    getDeployment: (cfg, projectId, deploymentId) => callThetaMcpTool(cfg, 'get_gpu_deployment', withProject(projectId, { deployment_id: deploymentId })),
    deploymentEvents: (cfg, projectId, deploymentId) => callThetaMcpTool(cfg, 'get_gpu_deployment_events', withProject(projectId, { deployment_id: deploymentId })),
    deploymentLogs: (cfg, projectId, deploymentId) => callThetaMcpTool(cfg, 'get_gpu_deployment_logs', withProject(projectId, { deployment_id: deploymentId })),
    createDeployment: async (cfg, projectId, req) => {
        if (!Number.isFinite(req.maxPricePerHourUsd) || req.maxPricePerHourUsd <= 0) {
            throw new Error('maxPricePerHourUsd is required: it is sent as Theta\'s provider-side hourly price cap');
        }
        const args = withProject(projectId, {
            name: req.name,
            display_name: req.displayName,
            deployment_template_id: req.deploymentTemplateId,
            resource_id: req.resourceId,
            region: req.region,
            container_image: req.containerImage,
            ssh_public_key: req.sshPublicKey,
            ssh_port: req.sshPort,
            http_port: req.httpPort,
            max_price_per_hour_usd: req.maxPricePerHourUsd,
            confirm: req.confirm === true
        });
        if (cfg.dryRun)
            return mutationPreview('create_gpu_deployment', args);
        requireConfirm('create_gpu_deployment', req.confirm);
        // Refuse before provisioning when the current listed price already exceeds the cap.
        const resource = await gpu.getResource(cfg, projectId, req.resourceId, req.region);
        const price = resource?.price_per_hour_usd ?? resource?.resource?.price_per_hour_usd;
        if (typeof price === 'number' && price > req.maxPricePerHourUsd) {
            throw new Error(`Resource ${req.resourceId} lists USD ${price}/h, above the approved cap of USD ${req.maxPricePerHourUsd}/h`);
        }
        return callThetaMcpTool(cfg, 'create_gpu_deployment', args);
    },
    lifecycle: async (cfg, projectId, action, deploymentId, confirm) => {
        const tool = `${action}_gpu_deployment`;
        const args = withProject(projectId, { deployment_id: deploymentId, confirm: confirm === true });
        if (cfg.dryRun)
            return mutationPreview(tool, args);
        requireConfirm(tool, confirm);
        return callThetaMcpTool(cfg, tool, args);
    }
};
export const billing = {
    balanceUsd: (cfg, projectId) => callThetaMcpTool(cfg, 'get_billing_balance', withProject(projectId)),
    usage: (cfg, projectId, startDate, endDate) => {
        for (const [label, value] of [['startDate', startDate], ['endDate', endDate]]) {
            if (value !== undefined && !/^\d{4}-\d{2}-\d{2}$/.test(value))
                throw new Error(`${label} must be YYYY-MM-DD`);
        }
        return callThetaMcpTool(cfg, 'get_billing_usage', withProject(projectId, { start_date: startDate, end_date: endDate }));
    },
    topUps: (cfg, projectId, page, number) => callThetaMcpTool(cfg, 'list_billing_top_ups', withProject(projectId, { page, number })),
    pricing: (cfg, projectId) => callThetaMcpTool(cfg, 'get_billing_pricing', withProject(projectId))
};
