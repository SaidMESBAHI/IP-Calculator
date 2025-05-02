import ipaddress

def get_network_info(ip, cidr):
    network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
    mask = str(network.netmask)

    return {
        "Adresse réseau": str(network.network_address),
        "Adresse de broadcast": str(network.broadcast_address),
        "Nombre d’hôtes": network.num_addresses - 2 if network.prefixlen < 31 else network.num_addresses,
        "Plage d’hôtes": f"{network.network_address + 1} - {network.broadcast_address - 1}" if network.prefixlen < 31 else "N/A",
        "Masque de sous-réseau": mask,
        "CIDR": f"/{network.prefixlen}"
    }
