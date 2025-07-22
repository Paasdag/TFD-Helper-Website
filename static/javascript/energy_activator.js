const conversion = {
    "low-carbon-activator": 55,
    "conductive-metallic-foil": 25,
    "heat-plasma-battery": 55,
    "polyatomic-ion-particle": 72
}

function calculate() {
    const value = parseInt(document.getElementById("input_value").value)
    
    if (isNaN(value) || value < 0) return

    for (const [id, rate] of Object.entries(conversion)){
        const output = value * rate
        const element = document.getElementById(id)
        if (element) element.innerText = output
    }
}
