# Wifi Mesh Tester
Visualizes the 802.11r handovers in your Mesh network (OpenWRT based or others).

Currently this is a very simple script, polling nmcli to get the current BSSID and showing some extra values.
It differs from other scripts and applications in a way that it focuses on showing handovers and possible issues with specific access points.

For a bit of extra user friendlyness, there is the possiblity to add a yaml file which resolves the BSSID into a friendly name:

```yaml
kitchen:
  - 11:22:33:44:55:A1
  - 11:22:33:44:55:A2
garage:
  - 77:88:99:AA:BB:C1
  - 77:88:99:AA:BB:C2
  - 77:88:99:AA:BB:C3
```
