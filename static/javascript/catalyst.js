const conversion = {
    "murky-energy-residue": 8,
    "macromolecule-biogel": 22,
    "mixed-energy-residue": 8,
    "advanced-neural-circut": 18
}

function calculate() {
    const catalystCount = parseInt(document.getElementById("catalystvalue").value)
    
    if (isNaN(catalystCount) || catalystCount < 0) return

    for (const [id, rate] of Object.entries(conversion)){
        const output = catalystCount * rate
        const element = document.getElementById(id)
        if (element) element.innerText = output
    }
}
