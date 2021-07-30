config = """
dci1:
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      b_device: borderleaf1
      b_int: Ethernet12
    - name: Ethernet2
      type: "1000base-t"
      b_device: borderleaf2
      b_int: Ethernet12
borderleaf1: 
  mlag: 
    - odd
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      mode: "tagged-all"
      b_device: borderleaf2
      b_int: Ethernet1
    - name: Ethernet2
      type: "1000base-t"
      mode: "tagged-all"
      b_device: borderleaf2
      b_int: Ethernet2
    - name: Ethernet3
      type: "1000base-t"
      b_device: spine1
      b_int: Ethernet6
    - name: Ethernet4
      type: "1000base-t"
      b_device: spine2
      b_int: Ethernet6
    - name: Ethernet5
      type: "1000base-t"
      b_device: spine3
      b_int: Ethernet6
    - name: Ethernet12
      type: "1000base-t"
      b_device: dci1
      b_int: Ethernet1
borderleaf2: 
  mlag: 
    - even
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      mode: "tagged-all"
      b_device: borderleaf1
      b_int: Ethernet1
    - name: Ethernet2
      type: "1000base-t"
      mode: "tagged-all"
      b_device: borderleaf1
      b_int: Ethernet2
    - name: Ethernet3
      type: "1000base-t"
      b_device: spine1
      b_int: Ethernet7
    - name: Ethernet4
      type: "1000base-t"
      b_device: spine2
      b_int: Ethernet7
    - name: Ethernet5
      type: "1000base-t"
      b_device: spine3
      b_int: Ethernet7
    - name: Ethernet12
      type: "1000base-t"
      b_device: dci1
      b_int: Ethernet2
spine1:
  device_type: "spine_veos"
  interfaces:
    - name: Ethernet2
      type: "1000base-t"
      b_device: leaf1
      b_int: Ethernet3
    - name: Ethernet3
      type: "1000base-t"
      b_device: leaf2
      b_int: Ethernet3
    - name: Ethernet4
      type: "1000base-t"
      b_device: leaf3
      b_int: Ethernet3
    - name: Ethernet5
      type: "1000base-t"
      b_device: leaf4
      b_int: Ethernet3
    - name: Ethernet6
      type: "1000base-t"
      b_device: borderleaf1
      b_int: Ethernet3
    - name: Ethernet7 
      type: "1000base-t"
      b_device: borderleaf2
      b_int: Ethernet3
spine2:
  interfaces:
    - name: Ethernet2
      type: "1000base-t"
      b_device: leaf1
      b_int: Ethernet4
    - name: Ethernet3
      type: "1000base-t"
      b_device: leaf2
      b_int: Ethernet4
    - name: Ethernet4
      type: "1000base-t"
      b_device: leaf3
      b_int: Ethernet4
    - name: Ethernet5
      type: "1000base-t"
      b_device: leaf4
      b_int: Ethernet4
    - name: Ethernet6
      type: "1000base-t"
      b_device: borderleaf1
      b_int: Ethernet4
    - name: Ethernet7 
      type: "1000base-t"
      b_device: borderleaf2
      b_int: Ethernet4
spine3:
  interfaces:
    - name: Ethernet2
      type: "1000base-t"
      b_device: leaf1
      b_int: Ethernet5
    - name: Ethernet3
      type: "1000base-t"
      b_device: leaf2
      b_int: Ethernet5
    - name: Ethernet4
      type: "1000base-t"
      b_device: leaf3
      b_int: Ethernet5
    - name: Ethernet5
      type: "1000base-t"
      b_device: leaf4
      b_int: Ethernet5
    - name: Ethernet6
      type: "1000base-t"
      b_device: borderleaf1
      b_int: Ethernet5
    - name: Ethernet7 
      type: "1000base-t"
      b_device: borderleaf2
      b_int: Ethernet5
leaf1:
  mlag: 
    - odd
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf2
      b_int: Ethernet1
    - name: Ethernet2
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf2
      b_int: Ethernet2
    - name: Ethernet3
      type: "1000base-t"
      b_device: spine1
      b_int: Ethernet2
    - name: Ethernet4
      type: "1000base-t"
      b_device: spine2
      b_int: Ethernet3
    - name: Ethernet5
      type: "1000base-t"
      b_device: spine3
      b_int: Ethernet4
leaf2:
  mlag:
    - even
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf1
      b_int: Ethernet1
    - name: Ethernet2
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf1
      b_int: Ethernet2
    - name: Ethernet3
      type: "1000base-t"
      b_device: spine1
      b_int: Ethernet2
    - name: Ethernet4
      type: "1000base-t"
      b_device: spine2
      b_int: Ethernet3
    - name: Ethernet5
      type: "1000base-t"
      b_device: spine3
      b_int: Ethernet4
leaf3:
  mlag: 
    - odd
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf4
      b_int: Ethernet1
    - name: Ethernet2
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf4
      b_int: Ethernet2
    - name: Ethernet3
      type: "1000base-t"
      b_device: spine1
      b_int: Ethernet2
    - name: Ethernet4
      type: "1000base-t"
      b_device: spine2
      b_int: Ethernet3
    - name: Ethernet5
      type: "1000base-t"
      b_device: spine3
      b_int: Ethernet4
leaf4:
  mlag: 
    - even
  interfaces:
    - name: Ethernet1
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf3
      b_int: Ethernet1
    - name: Ethernet2
      type: "1000base-t"
      mode: "tagged-all"
      b_device: leaf3
      b_int: Ethernet2
    - name: Ethernet3
      type: "1000base-t"
      b_device: spine1
      b_int: Ethernet2
    - name: Ethernet4
      type: "1000base-t"
      b_device: spine2
      b_int: Ethernet3
    - name: Ethernet5
      type: "1000base-t"
      b_device: spine3
      b_int: Ethernet4
"""
from types import TracebackType
from django.utils.text import slugify
import yaml
import json
from nautobot.dcim.models import Site, Device, Rack, Region, Cable, DeviceRole, DeviceType, Interface
from nautobot.ipam.models import Role, Prefix, IPAddress, VLAN
from nautobot.extras.models import CustomField, Job, Status
from nautobot.extras.models.customfields import ContentType
from nautobot.extras.jobs import Job, StringVar, IntegerVar, ObjectVar, BooleanVar
from nautobot.circuits.models import Provider, CircuitType, Circuit, CircuitTermination
import ipaddress
##########################
# credit to damien @ NTC #
CUSTOM_FIELDS = {
    "role": {"models": [Interface], "label": "Role"},
    "site_type": {"models": [Site], "label": "Type of Site"},
    "device_bgp": {"models": [Device], "label": "Device BGP ASN"}
}
def create_custom_fields():
    """Create all relationships defined in CUSTOM_FIELDS."""
    for cf_name, field in CUSTOM_FIELDS.items():
        try:
            cf = CustomField.objects.get(name=cf_name)
        except CustomField.DoesNotExist:
            cf = CustomField.objects.create(name=cf_name)
            if "label" in field:
                cf.label = field.get("label")
            cf.validated_save()
        for model in field["models"]:
            ct = ContentType.objects.get_for_model(model)
            cf.content_types.add(ct)
            cf.validated_save()
############################

# Most of this stuff is pretty much pulled from an NTC Job on the demo site. I filled in some of the blanks
IPv4Network = ipaddress.ip_network
class CreateAristaDC(Job):
    """Job to create a new site and datacenter pod."""

    class Meta:
        """Meta class for CreateAristaDC."""

        name = "Create a new Arista DataCenter"
        description = """
        Create a new Site  with N Spine, leaf switches, borderleaf switchs, and or a DCI switch.
        A new /22 will automatically be allocated from the 'Datacenter Global Pool' Prefix
        """
        label = "Arista_DataCenter"
        field_order = [
            "region",
            "dc_code",
            "dc_bgp",
            "spine_count",
            "leaf_count",
            "borderleaf",
            "dci",
        ]

    region = ObjectVar(model=Region)

    dc_code = StringVar(description="Name of the new DataCenter", label="DataCenter")
    
    spine_count = IntegerVar(description="Number of Spine Switches", label="Spine switches count", min_value=1, max_value=3)

    dc_bgp = IntegerVar(description="DataCenter BGP AS", label="DC BGP AS")

    leaf_count = IntegerVar(description="Number of Leaf Switches", label="Leaf switches count", min_value=1, max_value=4)

    borderleaf = BooleanVar(description="Does this DataCenter require Border Leaf switches?", label="borderleaf required")
    
    dci = BooleanVar(description="Does this DataCenter require an interconnect?", label="DCI required")
    
    def run(self, data=None, commit=None):
        """Main function for CreateDC."""
        self.devices = {}

        # ----------------------------------------------------------------------------
        # Initialize the database with all required objects
        # ----------------------------------------------------------------------------
        create_custom_fields()
        # create_relationships()
        # create_prefix_roles()

        # ----------------------------------------------------------------------------
        # Find or Create Site
        # ----------------------------------------------------------------------------
        dc_code = data["dc_code"].lower()
        region = data["region"]
        bgp = data["dc_bgp"]
        site_status = Status.objects.get_for_model(Site).get(slug="active")
        self.site, created = Site.objects.get_or_create(name=dc_code, region=region, slug=dc_code, status=site_status)
        self.site.custom_field_data["site_type"] = "DATACENTER"
        self.site.save()
        self.log_success(self.site, f"Site {dc_code} successfully created")

        # Creating MLAG VLAN
        vlan = VLAN.objects.get_or_create(
          name="MLAG_VLAN",
          vid=4096,
          status=site_status,
          site=self.site
        )
        # vlan.validated_save()
        self.log_success(obj=vlan, message="Created MLAG VLAN")

        vlan_4096_prefix = Prefix.objects.get_or_create(
          prefix="192.168.255.0/30",
          status=site_status,
        )
        # vlan_4096_prefix.validated_save()
        self.log_success(obj=vlan_4096_prefix, message="Created MLAG Prefix")
        
        # Reference Vars
        TOP_LEVEL_PREFIX_ROLE = "datacenter"
        SITE_PREFIX_SIZE = 22 
        RACK_HEIGHT = 42
        RACK_TYPE = "4-post-frame"
        ROLES = {
            "spine": {"device_type": "spine_veos"},
            "leaf": {"device_type": "leaf_veos"},
            "borderleaf": {"device_type": "leaf_veos"},
            "dci": {"device_type": "spine_veos"},
        }
        # Number of devices to provision
        ROLES["leaf"]["nbr"] = data["leaf_count"]
        ROLES["spine"]["nbr"] = data["spine_count"]
        if data["borderleaf"] == True:
            ROLES["borderleaf"]["nbr"] = 2
        else:
            ROLES["borderleaf"]["nbr"] = 0
        if data["dci"] == True:
            ROLES["dci"]["nbr"] = 1
        else:
            ROLES["dci"]["nbr"] = 0

        
        # ----------------------------------------------------------------------------
        # Allocate Prefixes for this DataCenter
        # ----------------------------------------------------------------------------
        # Search if there is already a POP prefix associated with this side
        # if not search the Top Level Prefix and create a new one
        dc_role, _ = Role.objects.get_or_create(name=dc_code, slug=dc_code)
        container_status = Status.objects.get_for_model(Prefix).get(slug="container")
        dc_prefix = Prefix.objects.filter(site=self.site, status=container_status, role=dc_role).first()

        if not dc_prefix:
            top_level_prefix = Prefix.objects.filter(
                role__slug=slugify(TOP_LEVEL_PREFIX_ROLE), status=container_status
            ).first()

            if not top_level_prefix:
                raise Exception("Unable to find the top level prefix to allocate a Network for this site")

            first_avail = top_level_prefix.get_first_available_prefix()
            prefix = list(first_avail.subnet(SITE_PREFIX_SIZE))[0]
            dc_prefix = Prefix.objects.create(prefix=prefix, site=self.site, status=container_status, role=dc_role)

        iter_subnet = IPv4Network(str(dc_prefix.prefix)).subnets(new_prefix=24)

        # Allocate the subnet by block of /24
        # mlag_peer = next(iter_subnet)
        overlay_loopback = next(iter_subnet)
        vtep_loopback = next(iter_subnet)
        underlay_p2p = next(iter_subnet)
        # dci_p2p = next(iter_subnet)

        dc_role, _ = Role.objects.get_or_create(name=dc_code, slug=dc_code)

        # mlag_peer_role, _ = Role.objects.get_or_create(name=f"{dc_code}_mlag_peer", slug=f"{dc_code}_mlag_peer")
        # Prefix.objects.get_or_create(
        #     prefix=str(mlag_peer),
        #     site=self.site,
        #     role=mlag_peer_role,
        #     status=container_status,
        # )
        # self.log_success(obj=mlag_peer, message="Created new mlag peer prefix")

        overlay_role, _ = Role.objects.get_or_create(name=f"{dc_code}_overlay", slug=f"{dc_code}_overlay")
        Prefix.objects.get_or_create(
            prefix=str(overlay_loopback),
            site=self.site,
            role=overlay_role,
            status=container_status,
        )
        self.log_success(obj=overlay_loopback, message="Created new overlay prefix")
        

        vtep_role, _ = Role.objects.get_or_create(name=f"{dc_code}_vtep_loopback", slug=f"{dc_code}_vtep_loopback")
        Prefix.objects.get_or_create(
            prefix=str(vtep_loopback),
            site=self.site,
            role=vtep_role,
            status=container_status,
        )
        self.log_success(obj=vtep_loopback, message="Created new vtep prefix")

        underlay_role, _ = Role.objects.get_or_create(name=f"{dc_code}_underlay_p2p", slug=f"{dc_code}_underlay_p2p")
        Prefix.objects.get_or_create(
            prefix=str(underlay_p2p), 
            site=self.site, 
            role=underlay_role, 
            status=container_status,
        )
        self.log_success(obj=underlay_p2p, message="Created new underlay p2p prefix")

        # dci_p2p_role, _ = Role.objects.get_or_create(name=f"{dc_code}_dci_p2p", slug=f"{dc_code}_dci_p2p")
        # Prefix.objects.get_or_create(
        #     prefix=str(dci_p2p),
        #     site=self.site,
        #     role=dci_p2p_role,
        #     status=container_status,
        # )
        # self.log_success(obj=dci_p2p, message="Created new dci p2p prefix")

        # ----------------------------------------------------------------------------
        # Create Racks
        # ----------------------------------------------------------------------------
        rack_status = Status.objects.get_for_model(Rack).get(slug="active")

        rack_name_spine = f"{dc_code}-spine-rr-1"
        rack = Rack.objects.get_or_create(
            name=rack_name_spine, site=self.site, u_height=RACK_HEIGHT, type=RACK_TYPE, status=rack_status
        )
        self.log_success(obj=rack_name_spine, message=f"Created Relay Rack {rack_name_spine}")

        if data["borderleaf"] == True: 
            rack_name_edge = f"{dc_code}-edge-rr-1"
            rack = Rack.objects.get_or_create(
                name=rack_name_edge, site=self.site, u_height=RACK_HEIGHT, type=RACK_TYPE, status=rack_status
            )
            self.log_success(obj=rack_name_edge, message=f"Created Relay Rack {rack_name_edge}")

        for i in range(1, ROLES["leaf"]["nbr"] + 1):
            rack_name = f"{dc_code}-leaf-rr-{i}"
            rack = Rack.objects.get_or_create(
                name=rack_name, site=self.site, u_height=RACK_HEIGHT, type=RACK_TYPE, status=rack_status
            )
            self.log_success(obj=rack_name, message=f"Created Relay Rack {rack_name}")

        # ----------------------------------------------------------------------------
        # Create Devices
        # ----------------------------------------------------------------------------
        for role, data in ROLES.items():
            for i in range(1, data.get("nbr", 2) + 1):
                if 'spine' in role:
                    rack_elevation = i + 1
                    rack_name = f"{dc_code}-spine-rr-1"
                    rack = Rack.objects.filter(name=rack_name, site=self.site).first()
                elif role == 'leaf':
                    rack_elevation = i + 1
                    rack_name = f"{dc_code}-leaf-rr-{i}"
                    rack = Rack.objects.filter(name=rack_name, site=self.site).first()
                elif role == 'borderleaf':
                    rack_elevation = i + 1
                    rack_name = f"{dc_code}-edge-rr-1"
                    rack = Rack.objects.filter(name=rack_name, site=self.site).first()
                elif 'dci' in role:
                    rack_elevation = i + 3
                    rack_name = f"{dc_code}-edge-rr-1"
                    rack = Rack.objects.filter(name=rack_name, site=self.site).first()

                device_name = f"{role}{i}-{dc_code}"

                device = Device.objects.filter(name=device_name).first()
                if device:
                    self.devices[device_name] = device
                    self.log_success(obj=device, message=f"Device {device_name} already present")
                    continue
                
                device_status = Status.objects.get_for_model(Device).get(slug="active")
                device_role, _ = DeviceRole.objects.get_or_create(name=role, slug=slugify(role))
                device = Device.objects.create(
                    device_type=DeviceType.objects.get(slug=data.get("device_type")),
                    name=device_name,
                    site=self.site,
                    status=device_status,
                    device_role=device_role,
                    rack=rack,
                    position=rack_elevation,
                    face="front",
                )

                device.clean()
                device.save()
                self.devices[device_name] = device
                self.log_success(device, f"Device {device_name} successfully created")

                # Building local context for various requirements per device
                lo0_prefix = Prefix.objects.get(role=overlay_role)
                # global LOCAL_CONTEXT
                LOCAL_CONTEXT = {
                  "prefix_list":[str(lo0_prefix)],
                }
                LOCAL_CONTEXT_JSON = json.dumps(LOCAL_CONTEXT, indent = 4)
                device.local_context = LOCAL_CONTEXT_JSON
                device.validated_save()
                self.log_success(device, f"Added local context on {device_name}")

                # Add the Devices specific BGP assignments
                if device_name == f"spine1-{dc_code}" or device_name == f"spine2-{dc_code}" or device_name == f"spine3-{dc_code}":
                    device._custom_field_data = {"device_bgp": bgp}
                    device.validated_save()
                    self.log_success(device, f"Added AS::{bgp} to Device {device_name}")

                elif device_name == f"leaf1-{dc_code}" or device_name == f"leaf2-{dc_code}":
                    leaf_bgp = bgp + 1
                    device._custom_field_data = {"device_bgp": leaf_bgp}
                    device.validated_save()
                    self.log_success(device, f"Added AS::{leaf_bgp} to Device {device_name}")

                elif device_name == f"leaf3-{dc_code}" or device_name == f"leaf4-{dc_code}":
                    leaf_bgp = bgp + 2
                    device._custom_field_data = {"device_bgp": leaf_bgp}
                    device.validated_save()
                    self.log_success(device, f"Added AS::{leaf_bgp} to Device {device_name}")

                elif device_name == f"borderleaf1-{dc_code}" or device_name == f"borderleaf2-{dc_code}":
                    borderleaf_bgp = bgp + 3
                    device._custom_field_data = {"device_bgp": borderleaf_bgp}
                    device.validated_save()
                    self.log_success(device, f"Added AS::{borderleaf_bgp} to Device {device_name}")

                elif device_name == f"dci1-{dc_code}":
                    dci_bgp = 65000
                    device._custom_field_data = {"device_bgp": dci_bgp}
                    device.validated_save()
                    self.log_success(device, f"Added AS::{dci_bgp} to Device {device_name}")


                # Create physical interfaces
                SWITCHES = yaml.load(config, Loader=yaml.FullLoader)
                dev_name = device_name.replace(f"-{dc_code}","")
                # for iface in SWITCHES[dev_name]['interfaces']:
                #     intf_name = Interface.objects.create(
                #             name=iface['name'],
                #             type="1000base-t",
                #             device=device, 
                #     )
                #     self.log_success(obj=intf_name, message=f"{intf_name} successfully created on {device_name}")
                if device_name == f"spine1-{dc_code}" or device_name == f"spine2-{dc_code}" or device_name == f"spine3-{dc_code}":
                  intf_number =  ROLES["leaf"]["nbr"] + ROLES["borderleaf"]["nbr"] + 1
                  for i in range(1, intf_number + 1):
                    int_name = Interface.objects.create(
                      name=f"Ethernet{i}",
                      type="1000base-t",
                      device=device,

                    )
                    self.log_success(obj=int_name, message=f"{int_name} successfully created on {device_name}")
                elif device_name == f"leaf1-{dc_code}" or device_name == f"leaf2-{dc_code}" or device_name == f"leaf3-{dc_code}" or device_name == f"leaf4-{dc_code}":
                   intf_number =  ROLES["spine"]["nbr"] + 2
                   for i in range(1, intf_number + 1):
                    int_name = Interface.objects.create(
                      name=f"Ethernet{i}",
                      type="1000base-t",
                      device=device,

                    )
                    self.log_success(obj=int_name, message=f"{int_name} successfully created on {device_name}")

                elif device_name == f"borderleaf1-{dc_code}" or device_name == f"borderleaf2-{dc_code}":
                  intf_number =  ROLES["spine"]["nbr"] + ROLES["dci"]["nbr"] + 2
                  for i in range(1, intf_number + 1):
                    int_name = Interface.objects.create(
                      name=f"Ethernet{i}",
                      type="1000base-t",
                      device=device,

                    )
                    self.log_success(obj=int_name, message=f"{int_name} successfully created on {device_name}")

                  if ROLES["dci"]["nbr"] != 0:
                    eth12 = Interface.objects.create(
                      name = "Ethernet12",
                      type= "1000base-t",
                      device = device,
                    )
                    self.log_success(obj=eth12, message=f"{eth12} successfully created on {device_name}")

                elif device_name == f"dci1-{dc_code}":
                  intf_number =  ROLES["borderleaf"]["nbr"]
                  for i in range(1, intf_number + 1):
                    int_name = Interface.objects.create(
                      name=f"Ethernet{i}",
                      type="1000base-t",
                      device=device,

                    )
                    self.log_success(obj=int_name, message=f"{int_name} successfully created on {device_name}")

                # LEAF MLAG Port Channel
                if device.device_role.slug == "leaf":
                    portchannel_intf = Interface.objects.create(
                        name="Port-Channel10", type="lag", mode="tagged-all", device=device
                    )
                    self.log_success(obj=portchannel_intf, message=f"{portchannel_intf} successfully created on {device_name}")
                    
                    # Thanks mcgoo298
                    eth1 = device.interfaces.get(name="Ethernet1")
                    eth2 = device.interfaces.get(name="Ethernet2")
                    po10 = device.interfaces.get(name="Port-Channel10")
                    eth1.lag = po10
                    eth1.mode = "tagged-all"
                    eth1.validated_save()
                    self.log_success(message=f"Moved {eth1} succesfully to {po10}")
                    eth2.lag = po10
                    eth2.mode = "tagged-all"
                    eth2.validated_save()
                    self.log_success(message=f"Moved {eth2} succesfully to {po10}")

                    # MLAG SVI
                    mlag_svi = Interface.objects.create(
                        name="Vlan4094", type="virtual", device=device
                    )
                    self.log_success(obj=mlag_svi, message=f"{mlag_svi} successfully created on {device_name}")

                    #######################################
                    # Creating IP addresses for MLAG Peer #
                    #######################################
                    if device_name == f"leaf1-{dc_code}" or device_name == f"leaf3-{dc_code}":
                        interface = Interface.objects.get(name="Vlan4094", device=device)
                        ip = IPAddress.objects.create(address='192.168.255.1/30', assigned_object=interface)
                        self.log_success(message=f"Created MLAG PEER address on {interface.device.name}::{interface}")

                    elif device_name == f"leaf2-{dc_code}" or device_name == f"leaf4-{dc_code}":
                        interface = Interface.objects.get(name="Vlan4094", device=device)
                        ip = IPAddress.objects.create(address='192.168.255.2/30', assigned_object=interface)
                        self.log_success(message=f"Created MLAG PEER address on {interface.device.name}::{interface}")


                # BORDERLEAF MLAG Port Channel
                if device.device_role.slug == "borderleaf":
                    portchannel_intf = Interface.objects.create(
                        name="Port-Channel10", type="lag", mode="tagged-all", device=device
                    )
                    self.log_success(obj=portchannel_intf, message=f"{portchannel_intf} successfully created on {device_name}")

                    eth1 = device.interfaces.get(name="Ethernet1")
                    eth2 = device.interfaces.get(name="Ethernet2")
                    po10 = device.interfaces.get(name="Port-Channel10")
                    eth1.lag = po10
                    eth1.validated_save()
                    self.log_success(message=f"Moved {eth1} succesfully to {po10}")
                    eth2.lag = po10
                    eth2.validated_save()
                    self.log_success(message=f"Moved {eth2} succesfully to {po10}")

                    # MLAG SVI
                    mlag_svi = Interface.objects.create(
                        name="Vlan4094", type="virtual", device=device
                    )
                    self.log_success(obj=mlag_svi, message=f"{mlag_svi} successfully created on {device_name}")

                    #######################################
                    # Creating IP addresses for MLAG Peer #
                    #######################################
                    if device_name == f"borderleaf1-{dc_code}":
                        interface = Interface.objects.get(name="Vlan4094", device=device)
                        ip = IPAddress.objects.create(address='192.168.255.1/30', assigned_object=interface)
                        self.log_success(message=f"Created MLAG PEER address on {interface.device.name}::{interface}")

                    elif device_name == f"borderleaf2-{dc_code}":
                        interface = Interface.objects.get(name="Vlan4094", device=device)
                        ip = IPAddress.objects.create(address='192.168.255.2/30', assigned_object=interface)
                        self.log_success(message=f"Created MLAG PEER address on {interface.device.name}::{interface}")



                # Generate Loopback0 interface and assign Loopback0 address
                loopback0_intf = Interface.objects.create(
                    name="Loopback0", type="virtual", device=device
                )
                self.log_success(obj=loopback0_intf, message=f"{loopback0_intf} successfully created on {device_name}")

                loopback0_prefix = Prefix.objects.get(
                    site=self.site, role__name=f"{dc_code}_overlay",
                )

                available_ips = loopback0_prefix.get_available_ips()
                lo0_address = list(available_ips)[0]
                loopback0_ip = IPAddress.objects.create(address=str(lo0_address), description=f"{device_name}::{loopback0_intf}", assigned_object=loopback0_intf)
                

                # Generate Loopback1 interface and assign Loopback1 address
                if device.device_role.slug == "leaf":
                    loopback1_intf = Interface.objects.create(
                        name="Loopback1", type="virtual", device=device
                    )
                    self.log_success(obj=loopback1_intf, message=f"{loopback1_intf} successfully created on {device_name}")

                    loopback1_prefix = Prefix.objects.get(
                        site=self.site,
                        role__name=f"{dc_code}_vtep_loopback",
                    )

                    available_ips = loopback1_prefix.get_available_ips()
                    lo1_address = list(available_ips)[0]
                    loopback1_ip = IPAddress.objects.create(address=str(lo1_address), description=f"{device_name}::{loopback1_intf}", assigned_object=loopback1_intf)

                elif device.device_role.slug == "borderleaf":
                    loopback1_intf = Interface.objects.create(
                        name="Loopback1", type="virtual", device=device
                    )
                    self.log_success(obj=loopback1_intf, message=f"{loopback1_intf} successfully created on {device_name}")

                    loopback1_prefix = Prefix.objects.get(
                        site=self.site,
                        role__name=f"{dc_code}_vtep_loopback",
                    )

                    available_ips = loopback1_prefix.get_available_ips()
                    lo1_address = list(available_ips)[0]
                    loopback1_ip = IPAddress.objects.create(address=str(lo1_address), description=f"{device_name}::{loopback1_intf}", assigned_object=loopback1_intf)

        #######################################
        # Creating Cables between interfaces  #
        #######################################
        for role, data in ROLES.items():
            for i in range(1, data.get("nbr", 2) + 1):
                device_name = f"{role}{i}-{dc_code}"
                device = Device.objects.get(name=device_name)
                dev_name = device_name.replace(f"-{dc_code}","")

                for iface in SWITCHES[dev_name]['interfaces']:
                  try:
                    interface = Interface.objects.get(name=iface['name'], device=device)
                    if interface.cable is None:
                        if "b_device" in iface.keys():
                            b_device = iface['b_device']
                            b_dev_name = f"{b_device}-{dc_code}"
                            bside_device = Device.objects.get(name=b_dev_name)
                            bside_interface = Interface.objects.get(name=iface['b_int'],device=bside_device, )
                            intf1 = interface
                            intf2 = bside_interface
                            status = Status.objects.get_for_model(Cable).get(slug="connected")
                            if intf1.cable or intf2.cable:
                                self.log_warning(
                                    message=f"Unable to create a P2P link between {intf1.device.name}::{intf1} and {intf2.device.name}::{intf2}"
                                )
                                return False
                            cable = Cable.objects.create(termination_a=intf1, termination_b=intf2, status=status)
                            cable.save()
                            self.log_success(message=f"Created a cable between {intf1.device.name}::{intf1} and {intf2.device.name}::{intf2}")
                            # Find Next available Network
                            if "mode" not in iface.keys():
                                P2P_PREFIX_SIZE = 31
                                prefix = Prefix.objects.filter(site=self.site, role__name=f"{dc_code}_underlay_p2p").first()
                                first_avail = prefix.get_first_available_prefix()
                                subnet = list(first_avail.subnet(P2P_PREFIX_SIZE))[0]

                                Prefix.objects.create(prefix=str(subnet))

                                # Create IP Addresses on both sides
                                ip1 = IPAddress.objects.create(address=str(subnet[0]), assigned_object=intf1)
                                ip2 = IPAddress.objects.create(address=str(subnet[1]), assigned_object=intf2)
                                self.log_success(message=f"Created a IP Address between {intf1.device.name}::{intf1} and {intf2.device.name}::{intf2}")
                  except Exception:
                    pass