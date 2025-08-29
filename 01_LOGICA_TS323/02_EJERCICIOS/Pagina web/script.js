let valorP = true;
let valorQ = true;
let equivalenciaSeleccionada = 1;

function negar(p) {
  return !p;
}
function yLogico(p, q) {
  return p && q;
}
function oLogico(p, q) {
  return p || q;
}
function implica(p, q) {
  return !p || q;
}
function bicondicional(p, q) {
  return (p && q) || (!p && !q);
}

function setVariable(variable, valor) {
  if (variable === "p") {
    valorP = valor;
    document.getElementById("p-true").classList.toggle("active", valor);
    document.getElementById("p-false").classList.toggle("active", !valor);
    document.getElementById("p-true").setAttribute("aria-pressed", valor);
    document.getElementById("p-false").setAttribute("aria-pressed", !valor);
  } else {
    valorQ = valor;
    document.getElementById("q-true").classList.toggle("active", valor);
    document.getElementById("q-false").classList.toggle("active", !valor);
    document.getElementById("q-true").setAttribute("aria-pressed", valor);
    document.getElementById("q-false").setAttribute("aria-pressed", !valor);
  }
}

function seleccionarEquivalencia(num, btn) {
  equivalenciaSeleccionada = num;
  document.querySelectorAll(".controls button").forEach((b) => {
    b.style.background = "#4CAF50";
  });
  btn.style.background = "#FF9800";
}

function formatearValor(valor) {
  return valor
    ? `<span class="result-value true-value">VERDADERO</span>`
    : `<span class="result-value false-value">FALSO</span>`;
}

function calcularEquivalencia() {
  const contenido = document.getElementById("contenido");
  let html = "";

  const equivalencias = {
    1: {
      titulo: "1. DOBLE NEGACIÓN",
      formula: "¬¬p ⇐⇒ p",
      expr1: () => negar(negar(valorP)),
      expr1_text: "¬¬p",
      expr2: () => valorP,
      expr2_text: "p",
      usaQ: false,
    },
    2: {
      titulo: "2. LEY CONMUTATIVA (CONJUNCIÓN)",
      formula: "(p ∧ q) ⇐⇒ (q ∧ p)",
      expr1: () => yLogico(valorP, valorQ),
      expr1_text: "p ∧ q",
      expr2: () => yLogico(valorQ, valorP),
      expr2_text: "q ∧ p",
      usaQ: true,
    },
    3: {
      titulo: "3. LEY CONMUTATIVA (DISYUNCIÓN)",
      formula: "(p ∨ q) ⇐⇒ (q ∨ p)",
      expr1: () => oLogico(valorP, valorQ),
      expr1_text: "p ∨ q",
      expr2: () => oLogico(valorQ, valorP),
      expr2_text: "q ∨ p",
      usaQ: true,
    },
    4: {
      titulo: "4. LEY DE MORGAN (DISYUNCIÓN)",
      formula: "¬(p ∨ q) ⇐⇒ (¬p ∧ ¬q)",
      expr1: () => negar(oLogico(valorP, valorQ)),
      expr1_text: "¬(p ∨ q)",
      expr2: () => yLogico(negar(valorP), negar(valorQ)),
      expr2_text: "(¬p ∧ ¬q)",
      usaQ: true,
    },
    5: {
      titulo: "5. LEY DE MORGAN (CONJUNCIÓN)",
      formula: "¬(p ∧ q) ⇐⇒ (¬p ∨ ¬q)",
      expr1: () => negar(yLogico(valorP, valorQ)),
      expr1_text: "¬(p ∧ q)",
      expr2: () => oLogico(negar(valorP), negar(valorQ)),
      expr2_text: "(¬p ∨ ¬q)",
      usaQ: true,
    },
    6: {
      titulo: "6. NEGACIÓN DE LA IMPLICACIÓN",
      formula: "¬(p ⊃ q) ⇐⇒ (p ∧ ¬q)",
      expr1: () => negar(implica(valorP, valorQ)),
      expr1_text: "¬(p → q)",
      expr2: () => yLogico(valorP, negar(valorQ)),
      expr2_text: "(p ∧ ¬q)",
      usaQ: true,
    },
    7: {
      titulo: "7. DEFINICIÓN DE IMPLICACIÓN",
      formula: "p ⊃ q ⇐⇒ (¬p ∨ q)",
      expr1: () => implica(valorP, valorQ),
      expr1_text: "p → q",
      expr2: () => oLogico(negar(valorP), valorQ),
      expr2_text: "(¬p ∨ q)",
      usaQ: true,
    },
    8: {
      titulo: "8. CONTRARRECÍPROCO",
      formula: "(p ⊃ q) ⇐⇒ (¬q ⊃ ¬p)",
      expr1: () => implica(valorP, valorQ),
      expr1_text: "(p → q)",
      expr2: () => implica(negar(valorQ), negar(valorP)),
      expr2_text: "(¬q → ¬p)",
      usaQ: true,
    },
    9: {
      titulo: "9. PRINCIPIO DE DOBLE IMPLICACIÓN",
      formula: "(p ⇐⇒ q) ⇐⇒ (p ⊃ q) ∧ (q ⊃ p)",
      expr1: () => bicondicional(valorP, valorQ),
      expr1_text: "(p ↔ q)",
      expr2: () => yLogico(implica(valorP, valorQ), implica(valorQ, valorP)),
      expr2_text: "(p → q) ∧ (q → p)",
      usaQ: true,
    },
  };

  const eq = equivalencias[equivalenciaSeleccionada];
  if (eq) {
    const resultado1 = eq.expr1();
    const resultado2 = eq.expr2();
    const sonEquivalentes = resultado1 === resultado2;

    html = `
                    <div class="equivalence-section">
                        <div class="equivalence-title">${eq.titulo}</div>
                        <div class="formula">${eq.formula}</div>
                        
                        <div class="calculation-result">
                            <h3 style="text-align: center; margin-bottom: 20px;">🧮 VALORES ACTUALES:</h3>
                            <div style="text-align: center; margin: 15px 0; font-size: 18px;">
                                <strong>P = ${
                                  valorP ? "VERDADERO" : "FALSO"
                                }</strong>
                                ${
                                  eq.usaQ
                                    ? ` | <strong>Q = ${
                                        valorQ ? "VERDADERO" : "FALSO"
                                      }</strong>`
                                    : ""
                                }
                            </div>
                            <div class="result-row">
                                <span class="result-expression">${
                                  eq.expr1_text
                                }</span>
                                ${formatearValor(resultado1)}
                            </div>
                            <div class="result-row">
                                <span class="result-expression">${
                                  eq.expr2_text
                                }</span>
                                ${formatearValor(resultado2)}
                            </div>
                            <div class="equivalence-check ${
                              sonEquivalentes ? "equivalent" : "not-equivalent"
                            }">
                                ${
                                  sonEquivalentes
                                    ? "✅ SON EQUIVALENTES"
                                    : "❌ NO SON EQUIVALENTES"
                                }
                            </div>
                        </div>
                    </div>
                `;
  }
  contenido.innerHTML = html;
}

window.onload = function () {
  seleccionarEquivalencia(1, document.querySelector(".controls button"));
  calcularEquivalencia();
};
