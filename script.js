class NumberGuessingGame {
    constructor() {
        this.categories = {
    /* ? */    'Divisor': [],
    /* ? */    'Misma raiz digital': [],
    /* 2 */    'Perfecto': [6,28],
    /* 4 */    'Cubo perfecto': [1,8,27,64],
    /* 9 */    'Altamente compuesto': [1,2,4,6,12,24,36,48,60],
    /* 9 */    'Prónico': [2,6,12,20,30,42,56,72,90],
    /* 10 */   'Fibonacci': [1,2,3,5,8,13,21,34,55,89],
    /* 10 */   'Cuadrado perfecto': [1,4,9,16,25,36,49,64,81,100],
    /* 11 */   'Multiplo de 9': [9,18,27,36,45,54,63,72,81,90,99],
    /* 12 */   'Multiplo de 8': [8,16,24,32,40,48,56,64,72,80,88,96],
    /* 13 */   'Triangular': [1,3,6,10,15,21,28,36,45,55,66,78,91],
    /* 14 */   'Multiplo de 7': [7,14,21,28,35,42,49,56,63,70,77,84,91,98],
    /* 16 */   'Multiplo de 6': [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96],
    /* 18 */   'Palindrome': [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99],
    /* 18 */   'Numero feliz': [10,13,19,23,28,31,32,44,49,68,70,79,82,86,91,94,97,100],
    /* 20 */   'Multiplo de 5': [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
    /* 22 */   'Abundante': [12,18,20,24,30,36,40,42,48,54,56,60,66,70,72,78,80,84,88,90,96,100],
    /* 24 */   'Harshad': [10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100],
    /* 25 */   'Primo': [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97],
    /* 25 */   'Multiplo de 4': [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100],
    /* 33 */   'Multiplo de 3': [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99],
    /* 34 */   'Numero regular': [1,2,3,4,5,6,8,9,10,12,15,16,18,20,24,25,27,30,32,36,40,45,48,50,54,60,64,72,75,80,81,90,96,100],
    /* 34 */   'Semi primo': [4,6,9,10,14,15,21,22,25,26,33,34,35,38,39,46,49,51,55,57,58,62,65,69,74,77,82,85,86,87,91,93,94,95],
    /* 36 */   'Suma de digitos prima': [2,3,5,7,11,12,14,16,20,21,23,25,29,30,32,34,38,41,43,47,50,52,56,58,61,65,67,70,74,76,83,85,89,92,94,98],
    /* 45 */   'Dígitos ascendentes' : [1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,23,24,25,26,27,28,29,34,35,36,37,38,39,45,46,47,48,49,56,57,58,59,67,68,69,78,79,89], 
    /* 50 */   'Par': [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100],
    /* 50 */   'Impar': [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99],
    /* 74 */   'Compuesto': [4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30,32,33,34,35,36,38,39,40,42,44,45,46,48,49,50,51,52,54,55,56,57,58,60,62,63,64,65,66,68,69,70,72,74,75,76,77,78,80,81,82,84,85,86,87,88,90,91,92,93,94,95,96,98,99,100],
    /* 76 */   'Deficiente': [1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19,21,22,23,25,26,27,29,31,32,33,34,35,37,38,39,41,43,44,45,46,47,49,50,51,52,53,55,57,58,59,61,62,63,64,65,67,68,69,71,73,74,75,76,77,79,81,82,83,85,86,87,89,91,92,93,94,95,97,98,99],
    /* 100 */  'Natural': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
        };

        this.categoryDescriptions = {
            'Divisor': 'Números que dividen exactamente al número secreto sin dejar residuo.<br><br>Ejemplo: Si el número secreto fuera 24, entonces 8 es divisor porque 24÷8 = 3',
            'Misma raiz digital': 'Números cuya raíz digital (suma repetida hasta un dígito) sea igual a la del número secreto.<br><br>Ejemplo: 16→1+6=7, 25→2+5=7, 34→3+4=7 (todos tienen raíz digital 7)',
            'Perfecto': 'Un número perfecto es igual a la suma de todos sus divisores propios (excluyendo el número mismo).<br><br>Ejemplo: 6 → divisores propios: 1, 2, 3 → suma: 1+2+3 = 6',
            'Cubo perfecto': 'Un número que es el cubo de un entero (n³).<br><br>Ejemplo: 27 → 3³ = 3×3×3 = 27',
            'Altamente compuesto': 'Un número con más divisores que cualquier número positivo menor que él.<br><br>Ejemplo: 12 → tiene 6 divisores (1,2,3,4,6,12), más que cualquier número menor',
            'Prónico': 'Un número que es el producto de dos enteros consecutivos (n × (n+1)).<br><br>Ejemplo: 20 → 4×5 = 20 (4 y 5 son consecutivos)',
            'Fibonacci': 'Números de la famosa secuencia donde cada término es la suma de los dos anteriores.<br><br>Ejemplo: 13 → en la secuencia: 1,1,2,3,5,8,13... donde 13 = 5+8',
            'Cuadrado perfecto': 'Un número que es el cuadrado de un entero (n²).<br><br>Ejemplo: 49 → 7² = 7×7 = 49',
            'Multiplo de 9': 'Números divisibles por 9.<br><br>Ejemplo: 54 → 54÷9 = 6 (exacto)',
            'Multiplo de 8': 'Números divisibles por 8.<br><br>Ejemplo: 56 → 56÷8 = 7 (exacto)',
            'Triangular': 'Un número triangular representa la suma de los primeros n números enteros consecutivos (n × (n+1) / 2).<br><br>Ejemplo: 15 → suma de 1+2+3+4+5 = 15',
            'Multiplo de 7': 'Números divisibles por 7.<br><br>Ejemplo: 42 → 42÷7 = 6 (exacto)',
            'Multiplo de 6': 'Números divisibles por 6.<br><br>Ejemplo: 36 → 36÷6 = 6 (exacto)',
            'Palindrome': 'Números que se leen igual de izquierda a derecha y de derecha a izquierda.<br><br>Ejemplo: 77 → se lee igual en ambas direcciones',
            'Numero feliz': 'Un número que eventualmente llega a 1 cuando se reemplaza repetidamente por la suma de los cuadrados de sus dígitos.<br><br>Ejemplo: 19 → 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1',
            'Multiplo de 5': 'Números divisibles por 5.<br><br>Ejemplo: 85 → 85÷5 = 17 (exacto)',
            'Abundante': 'Un número menor que la suma de todos sus divisores propios.<br><br>Ejemplo: 18 → divisores propios: 1,2,3,6,9 → suma: 21 > 18',
            'Harshad': 'Un número divisible por la suma de sus dígitos.<br><br>Ejemplo: 84 → suma de dígitos: 8+4=12 → 84÷12 = 7 (exacto)',
            'Primo': 'Un número natural mayor que 1 que solo tiene dos divisores: 1 y él mismo.<br><br>Ejemplo: 37 → solo es divisible por 1 y 37',
            'Multiplo de 4': 'Números divisibles por 4.<br><br>Ejemplo: 76 → 76÷4 = 19 (exacto)',
            'Multiplo de 3': 'Números divisibles por 3.<br><br>Ejemplo: 63 → 63÷3 = 21 (exacto)',
            'Numero regular': 'Un número cuyos únicos factores primos son 2, 3 y 5.<br><br>Ejemplo: 48 → 48 = 2⁴×3¹ (solo factores 2 y 3)',
            'Semi primo': 'Un número que es el producto de exactamente dos números primos (no necesariamente distintos).<br><br>Ejemplo: 35 → 5×7 = 35 (producto de dos primos)',
            'Suma de digitos prima': 'Números cuya suma de dígitos es primo.<br><br>Ejemplo: 29 → 2+9=11 (primo), 38 → 3+8=11 (primo)',
            'Dígitos ascendentes': 'Los dígitos van en orden creciente.<br><br>Ejemplo: 12, 18, 27, 34',
            'Par': 'Números divisibles por 2.<br><br>Ejemplo: 78 → 78÷2 = 39 (exacto)',
            'Impar': 'Números no divisibles por 2.<br><br>Ejemplo: 73 → no es divisible por 2',
            'Compuesto': 'Un número natural mayor que 1 que no es primo.<br><br>Ejemplo: 91 → 91 = 7×13 (tiene más divisores que 1 y él mismo)',
            'Deficiente': 'Un número mayor que la suma de todos sus divisores propios.<br><br>Ejemplo: 17 → divisores propios: 1 → suma: 1 < 17',
            'Natural': 'Números enteros positivos (1, 2, 3, 4, ...).<br><br>Ejemplo: 95 → es un número entero positivo',
        };

        this.secretNumber = this.generateSecretNumber();
        this.guessedNumbers = [];
        this.adjacencyMatrix = {};
        this.gameWon = false;
        this.pinnedTooltip = null;

        this.initializeDynamicCategories();
        this.initializeEventListeners();
        this.showMessage('¡Nuevo juego iniciado! Adivina el número secreto.', 'info');
    }

    generateSecretNumber() {
        return Math.floor(Math.random() * 100) + 1;
    }

    calculateDigitalRoot(num) {
        while (num >= 10) {
            let sum = 0;
            while (num > 0) {
                sum += num % 10;
                num = Math.floor(num / 10);
            }
            num = sum;
        }
        return num;
    }

    initializeDynamicCategories() {
        // Inicializar divisores
        this.categories.Divisor = [];
        for (let n = 1; n <= 100; n++) {
            if (this.secretNumber % n === 0) {
                this.categories.Divisor.push(n);
            }
        }

        // Inicializar números con misma raíz digital
        const secretRoot = this.calculateDigitalRoot(this.secretNumber);
        this.categories['Misma raiz digital'] = [];
        for (let n = 1; n <= 100; n++) {
            if (this.calculateDigitalRoot(n) === secretRoot) {
                this.categories['Misma raiz digital'].push(n);
            }
        }

        this.adjacencyMatrix[this.secretNumber] = {};
    }

    initializeEventListeners() {
        const numberInput = document.getElementById('numberInput');
        const guessBtn = document.getElementById('guessBtn');
        const resetBtn = document.getElementById('resetBtn');

        guessBtn.addEventListener('click', () => this.makeGuess());
        resetBtn.addEventListener('click', () => this.resetGame());
        
        numberInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.makeGuess();
            }
        });
    }

    makeGuess() {
        const input = document.getElementById('numberInput');
        const guess = parseInt(input.value);

        if (!this.isValidGuess(guess)) return;

        if (guess === this.secretNumber) {
            this.gameWon = true;
            this.showMessage(`🎉 ¡Felicitaciones! Adivinaste el número ${this.secretNumber}!`, 'success');
            this.updateMatrix();
            input.value = '';
            return;
        }

        if (this.guessedNumbers.includes(guess)) {
            this.showMessage('Ya probaste ese número', 'warning');
            return;
        }

        // Buscar categorías compartidas
        const sharedCategories = this.findSharedCategories(guess, this.secretNumber);
        
        if (sharedCategories.length > 0) {
            this.guessedNumbers.push(guess);
            this.updateAdjacencyMatrix(guess, sharedCategories);
            this.updateMatrix();
        } else {
            this.showMessage(`El número ${guess} no comparte categorías con el número secreto`, 'info');
        }

        input.value = '';
    }

    isValidGuess(guess) {
        if (isNaN(guess) || guess < 1 || guess > 100) {
            this.showMessage('Por favor ingresa un número válido entre 1 y 100', 'warning');
            return false;
        }

        if (this.gameWon) {
            this.showMessage('¡Ya ganaste! Usa "Nuevo Juego" para comenzar otra partida', 'info');
            return false;
        }

        return true;
    }

    findSharedCategories(guess, secret) {
        const shared = [];
        for (const [category, members] of Object.entries(this.categories)) {
            if (members.includes(secret) && members.includes(guess)) {
                shared.push(category);
            }
        }
        return shared;
    }

    updateAdjacencyMatrix(guess, sharedCategories) {
        // Agregar nueva categoría encontrada
        for (const category of sharedCategories) {
            // Actualizar todas las entradas existentes con esta nueva categoría
            for (const number in this.adjacencyMatrix) {
                const num = parseInt(number);
                this.adjacencyMatrix[number][category] = this.categories[category].includes(num);
            }

            // Crear entrada para el nuevo guess
            if (!this.adjacencyMatrix[guess]) {
                this.adjacencyMatrix[guess] = {};
            }

            // Llenar el guess con todas las categorías existentes
            for (const existingCategory in this.adjacencyMatrix[this.secretNumber]) {
                this.adjacencyMatrix[guess][existingCategory] = this.categories[existingCategory].includes(guess);
            }

            // Agregar la nueva categoría al guess
            this.adjacencyMatrix[guess][category] = true;
        }

        // Ordenar las categorías según el orden original
        const categoryOrder = Object.keys(this.categories);
        for (const number in this.adjacencyMatrix) {
            const sortedCategories = {};
            categoryOrder.forEach(cat => {
                if (this.adjacencyMatrix[number][cat] !== undefined) {
                    sortedCategories[cat] = this.adjacencyMatrix[number][cat];
                }
            });
            this.adjacencyMatrix[number] = sortedCategories;
        }
    }

    updateMatrix() {
        const container = document.getElementById('matrixContainer');
        
        if (Object.keys(this.adjacencyMatrix).length === 0 || 
            Object.keys(this.adjacencyMatrix[this.secretNumber]).length === 0) {
            container.innerHTML = '<div class="empty-state">Ingresa tu primer número para comenzar a revelar las categorías compartidas</div>';
            return;
        }

        const numbers = Object.keys(this.adjacencyMatrix);
        const categories = Object.keys(this.adjacencyMatrix[this.secretNumber]);

        let html = '<table class="matrix-table fade-in">';
        
        // Header
        html += '<thead><tr><th>Categoría</th>';
        numbers.forEach(num => {
            const displayNum = (num == this.secretNumber && !this.gameWon) ? 'x' : num;
            const cellClass = num == this.secretNumber ? 'secret-number' : 'guessed-number';
            html += `<th class="${cellClass}">${displayNum}</th>`;
        });
        html += '</tr></thead>';

        // Body
        html += '<tbody>';
        categories.forEach(category => {
            const description = this.categoryDescriptions[category] || 'Descripción no disponible';
            html += `<tr><td>
                <span class="category-name">${category}</span>
                <span class="info-icon" data-category="${category}" data-description="${description.replace(/"/g, '&quot;')}">ℹ️</span>
            </td>`;
            numbers.forEach(num => {
                const value = this.adjacencyMatrix[num][category];
                const symbol = value ? '<span class="check-mark">✔</span>' : '<span class="cross-mark">·</span>';
                const cellClass = num == this.secretNumber ? 'secret-number' : 'guessed-number';
                html += `<td class="${cellClass}">${symbol}</td>`;
            });
            html += '</tr>';
        });
        html += '</tbody>';

        html += '</table>';
        container.innerHTML = html;
        
        // Crear tooltips fuera del contenedor de la tabla
        categories.forEach(category => {
            const description = this.categoryDescriptions[category] || 'Descripción no disponible';
            const tooltipElement = document.createElement('div');
            tooltipElement.className = 'tooltip';
            tooltipElement.id = `tooltip-${category.replace(/\s+/g, '-')}`;
            tooltipElement.innerHTML = `<div class="tooltip-content">${description}</div>`;
            document.body.appendChild(tooltipElement);
        });
        
        this.initializeTooltips();
    }

    initializeTooltips() {
        const infoIcons = document.querySelectorAll('.info-icon');
        
        // Cerrar tooltip al hacer click fuera
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.info-icon') && !e.target.closest('.tooltip')) {
                if (this.pinnedTooltip) {
                    this.pinnedTooltip.classList.remove('show', 'pinned');
                    this.pinnedTooltip = null;
                }
            }
        });
        
        infoIcons.forEach(icon => {
            const category = icon.dataset.category;
            const tooltipId = `tooltip-${category.replace(/\s+/g, '-')}`;
            const tooltip = document.getElementById(tooltipId);
            
            if (!tooltip) return;
            
            // Función para posicionar el tooltip
            const positionTooltip = (show = false) => {
                if (show) {
                    const iconRect = icon.getBoundingClientRect();
                    const tooltipRect = tooltip.getBoundingClientRect();
                    const viewportWidth = window.innerWidth;
                    const viewportHeight = window.innerHeight;
                    
                    let left = iconRect.right + 10;
                    let top = iconRect.top + (iconRect.height / 2) - (tooltipRect.height / 2);
                    
                    // Ajustar si se sale por la derecha
                    if (left + tooltipRect.width > viewportWidth - 20) {
                        left = iconRect.left - tooltipRect.width - 10;
                    }
                    
                    // Ajustar si se sale por arriba o abajo
                    if (top < 20) top = 20;
                    if (top + tooltipRect.height > viewportHeight - 20) {
                        top = viewportHeight - tooltipRect.height - 20;
                    }
                    
                    tooltip.style.left = `${left}px`;
                    tooltip.style.top = `${top}px`;
                }
            };
            
            // Hover events
            icon.addEventListener('mouseenter', () => {
                if (this.pinnedTooltip !== tooltip) {
                    tooltip.classList.add('show');
                    positionTooltip(true);
                }
            });
            
            icon.addEventListener('mouseleave', () => {
                if (!tooltip.classList.contains('pinned')) {
                    tooltip.classList.remove('show');
                }
            });
            
            tooltip.addEventListener('mouseenter', () => {
                if (!tooltip.classList.contains('pinned')) {
                    tooltip.classList.add('show');
                }
            });
            
            tooltip.addEventListener('mouseleave', () => {
                if (!tooltip.classList.contains('pinned')) {
                    tooltip.classList.remove('show');
                }
            });
            
            // Click event
            icon.addEventListener('click', (e) => {
                e.stopPropagation();
                
                // Cerrar tooltip previamente fijado
                if (this.pinnedTooltip && this.pinnedTooltip !== tooltip) {
                    this.pinnedTooltip.classList.remove('show', 'pinned');
                }
                
                if (tooltip.classList.contains('pinned')) {
                    // Si ya está fijado, desfijarlo
                    tooltip.classList.remove('pinned');
                    this.pinnedTooltip = null;
                } else {
                    // Fijarlo
                    tooltip.classList.add('show', 'pinned');
                    positionTooltip(true);
                    this.pinnedTooltip = tooltip;
                }
            });
            
            tooltip.addEventListener('click', (e) => {
                e.stopPropagation();
            });
        });
    }

    showMessage(text, type) {
        const messageEl = document.getElementById('message');
        messageEl.textContent = text;
        messageEl.className = `message ${type} fade-in`;
        messageEl.style.display = 'block';
        
        setTimeout(() => {
            messageEl.style.display = 'none';
        }, 4000);
    }

    resetGame() {
        this.secretNumber = this.generateSecretNumber();
        this.guessedNumbers = [];
        this.adjacencyMatrix = {};
        this.gameWon = false;
        this.pinnedTooltip = null;
        
        // Limpiar tooltips existentes
        const existingTooltips = document.querySelectorAll('.tooltip');
        existingTooltips.forEach(tooltip => tooltip.remove());
        
        this.initializeDynamicCategories();
        
        document.getElementById('message').style.display = 'none';
        document.getElementById('numberInput').value = '';
        
        this.updateMatrix();
        this.showMessage('¡Nuevo juego iniciado! Adivina el número secreto.', 'info');
    }
}

// Inicializar el juego cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
    new NumberGuessingGame();
});