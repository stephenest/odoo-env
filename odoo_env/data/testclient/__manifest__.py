#!/usr/bin/env python
{
    "name": "testclient",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "category": "Hidden",
    "summary": "Test Client Configuration",
    "description": """
        Test Client for Odoo Environment
    """,
    # Here begins docker-odoo-environment manifest
    "odoo-license": "CE",
    "port": "8069",
    "env-ver": "2",
    "config": [
        "workers = 2",
        "max_cron_threads = 1",
    ],
    "git-repos": [
        "https://github.com/OCA/web.git",
        "https://github.com/OCA/server-tools.git",
    ],
    "docker-images": [
        "odoo odoo:16.0",
        "postgres postgres:14",
    ]
}