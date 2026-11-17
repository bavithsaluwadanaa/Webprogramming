"use strict";

const form = document.querySelector("#bill-form");
const items = document.querySelector("#items");
const errors = document.querySelector("#errors");
const result = document.querySelector("#result");

function addItem(name = "", price = "") {
  const row = document.createElement("div");
  row.className = "item-row";
  row.innerHTML = `<input class="item-name" aria-label="Menu item" placeholder="Menu item" value="${name}"><input class="item-price" aria-label="Item price" type="number" min="0" step="0.01" placeholder="Price" value="${price}"><button type="button" class="secondary remove-item">Remove</button>`;
  items.append(row);
}

function splitBill(subtotal) {
  const people = Number(document.querySelector("#people").value);
  const tipRate = Number(document.querySelector("#tip").value);
  const issues = [];
  if (!Number.isInteger(people) || people < 1) issues.push("Enter a whole number of people greater than zero.");
  if (!Number.isFinite(subtotal) || subtotal < 0) issues.push("Enter valid, non-negative amounts.");
  if (issues.length) { errors.textContent = issues.join(" "); result.textContent = ""; return; }
  errors.textContent = "";
  const tip = subtotal * tipRate / 100;
  const total = subtotal + tip;
  result.innerHTML = `<h2>Bill summary</h2><p>Subtotal: ${subtotal.toFixed(2)}</p><p>Tip: ${tip.toFixed(2)}</p><p>Total: ${total.toFixed(2)}</p><p>Each person pays: <strong>${(total / people).toFixed(2)}</strong></p>`;
}

addItem();
document.querySelector("#add-item").addEventListener("click", () => addItem());
items.addEventListener("click", event => { if (event.target.matches(".remove-item")) event.target.closest(".item-row").remove(); });
form.addEventListener("submit", event => {
  event.preventDefault();
  const priceFields = [...document.querySelectorAll(".item-price")];
  const prices = priceFields.map(field => Number(field.value));
  const invalid = priceFields.some(field => field.value.trim() === "" || !Number.isFinite(Number(field.value)) || Number(field.value) < 0);
  if (!priceFields.length || invalid) { errors.textContent = "Add at least one menu item and enter a valid price for each."; result.textContent = ""; return; }
  splitBill(prices.reduce((sum, value) => sum + value, 0));
});
document.querySelector("#simple-calculate").addEventListener("click", () => {
  const value = document.querySelector("#total").value;
  if (value.trim() === "") { errors.textContent = "Enter a total bill amount first."; return; }
  splitBill(Number(value));
});
