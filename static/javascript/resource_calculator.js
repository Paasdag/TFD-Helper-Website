const conversionsMap = {
  energy_activator: [
    { name: "Low-carbon Activator", labelId: "value_1", valueId: "value_1", rate: 55 },
    { name: "Conductive Metallic Foil", labelId: "value_2", valueId: "value_2", rate: 25 },
    { name: "Heat-plasma Battery", labelId: "value_3", valueId: "value_3", rate: 55 },
    { name: "Polyatomic Ion Particle", labelId: "value_4", valueId: "value_4", rate: 72 }
  ],
  catalyst: [
    { name: "Murky Energy Residue", labelId: "name_1", valueId: "value_1", rate: 8 },
    { name: "Macromolecule Biogel", labelId: "name_2", valueId: "value_2", rate: 22 },
    { name: "Mixed Energy Residue", labelId: "name_3", valueId: "value_3", rate: 8 },
    { name: "Advanced Neural Circut", labelId: "name_4", valueId: "value_4", rate: 18 }
  ]
}

function calculate() {
    const selectedPage = document.getElementById("conversion_selector").value
    const inputValue = parseInt(document.getElementById("input_value").value)
    if (isNaN(inputValue) || inputValue < 0) return

    const conversion = conversionsMap[selectedPage]
    if (!conversion) return

    for (const { name, labelId, valueId, rate } of conversion) {
      const labelElem = document.getElementById(labelId)
      if (labelElem) labelElem.innerText = name

      const valueElem = document.getElementById(valueId)
      if (valueElem) valueElem.innerText = inputValue * rate
    }
}
