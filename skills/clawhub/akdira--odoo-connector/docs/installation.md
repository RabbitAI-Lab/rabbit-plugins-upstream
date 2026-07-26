# Installation Guide

This guide covers everything you need to install and configure the Odoo Connector skill for OpenClaw, including prerequisites, environment setup, and initial configuration.

## Prerequisites

Before installing the Odoo Connector skill, ensure your environment meets the following requirements:

### System Requirements

- **Python 3.8 or higher** — The skill uses Python's built-in `xmlrpc.client` module, which is included in the standard library. No additional Python packages are required for basic operations.
- **OpenClaw CLI** — The skill runs as an OpenClaw agent skill. Make sure OpenClaw is installed and configured on your system.
- **Network access** — Your machine must be able to reach the target Odoo instance over HTTPS (port 443) or HTTP (port 8080 for development environments).

### Odoo Server Requirements

The skill works with the following Odoo versions:

- **Odoo 17** (Community and Enterprise)
- **Odoo 18** (Community and Enterprise)
- **Odoo 19** (Community and Enterprise)

Your Odoo instance must have:

- XML-RPC API enabled (this is enabled by default in all standard Odoo installations)
- At least one user account with appropriate access rights for the operations you plan to perform
- A known database name (the exact database name, case-sensitive)

### Verifying Odoo XML-RPC Availability

You can quickly test if XML-RPC is available on your Odoo instance by running:

```bash
curl -s https://your-odoo-instance.com/xmlrpc/2/common -d '<?xml version="1.0"?><methodCall><methodName>version</methodName></methodCall>'
```

If you receive an XML response with version information, XML-RPC is working correctly.

## Installing via OpenClaw

The recommended installation method is through the OpenClaw skill registry:

```bash
openclaw skills install @akdira/odoo-connector
```

This command downloads the skill, places it in your local skills directory, and registers it with the OpenClaw agent system. After installation, the skill is immediately available for use.

### Verifying Installation

After installation, verify the skill is available:

```bash
openclaw skills list | grep odoo-connector
```

You should see the skill listed with its version number and description.

## Manual Installation

If you prefer to install the skill manually (for development or custom modifications), you can clone the repository directly:

```bash
cd ~/.openclaw/workspace/skills/
git clone https://github.com/akdira/odoo-connector.git
```

The skill will be automatically detected by OpenClaw on the next restart or skill refresh.

## Configuration

### Environment Variables

The skill reads Odoo connection parameters from environment variables. This is the recommended approach for managing credentials securely:

```bash
export ODOO_URL="https://your-odoo-instance.com"
export ODOO_DB="your_database_name"
export ODOO_USERNAME="your_api_user"
export ODOO_PASSWORD="your_api_key"
```

**Important:** Never commit credentials to version control. Always use environment variables or a secure secrets manager.

### Using an API Key Instead of Password

For production environments, it is strongly recommended to use an Odoo API key instead of a user password. API keys can be revoked independently and have more granular control.

To generate an API key in Odoo:

1. Log in to your Odoo instance as the user who will be used for API access
2. Go to **Settings** → **Users & Companies** → **Users**
3. Select your user account
4. Click on the **API Keys** tab (or look for "Allowed Devices" section)
5. Click **New API Key**
6. Give it a descriptive name (e.g., "OpenClaw Integration")
7. Copy the generated key and store it securely

Use this API key as the `ODOO_PASSWORD` value instead of your account password.

### Connection Through a Reverse Proxy

If your Odoo instance is behind a reverse proxy (Traefik, nginx, Caddy), ensure the proxy is configured to:

- Forward the `/xmlrpc/*` paths to the Odoo backend
- Support the XML-RPC content type (`text/xml`)
- Have appropriate timeout settings for long-running operations (at least 120 seconds)
- Use HTTPS with a valid TLS certificate

Example nginx configuration snippet:

```nginx
location /xmlrpc/ {
    proxy_pass http://odoo-backend:8069;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_read_timeout 120s;
    proxy_connect_timeout 10s;
}
```

### Docker Deployment

If your Odoo instance runs in Docker (which is common for Akdira deployments), the XML-RPC endpoints are automatically exposed on the Odoo container's port 8069. Ensure your Docker network configuration allows the OpenClaw agent to reach the Odoo container.

For Akdira VPS deployments, all services are connected via the `akdira-network` bridge network, so connectivity is automatic.

## Post-Installation Verification

After installation and configuration, run a quick connection test to verify everything is working:

```bash
python3 scripts/test-connection.py
```

If the script reports a successful connection and shows your Odoo version, the installation is complete and working correctly.

## Troubleshooting Installation

If you encounter issues during installation, refer to the [Troubleshooting Guide](troubleshooting.md) for common errors and their solutions.
