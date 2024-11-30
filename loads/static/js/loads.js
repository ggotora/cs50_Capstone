const tableRow = document.querySelectorAll('.table-row');

tableRow.forEach(el => {
    el.addEventListener('click', () => {
        window.location = el.dataset.href
    })
})

