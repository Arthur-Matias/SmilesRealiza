<script>
    export let paymentProgression;
    export let miles;
    export let buyMiles;
</script>

<div class="progression-bar">
    <div style='width: {paymentProgression}%' class="payment-progression"><p>Forma de Pagamento</p></div>
    <div style='width: {miles}%' class="miles"><p>Milhas Acumuladas</p></div>
    <div style='width: {buyMiles}%' class="buy-miles"><p>Comprando Milhas</p></div>
    <div class="goal">
        <i class="fas fa-certificate"></i>
    </div>
</div>

<style>
    .progression-bar{
        display: flex;
        position: relative;
        width: 100%;
        height: 1rem;
        background-color: #C4C4C4;
        z-index: 1;
    }
    .payment-progression{
        height: 100%;
        background-color: var(--main-color);
        color: var(--main-color);
    }
    .progression-bar> div > p{
        margin-top: 1rem;
        font-weight: 600;
    }
    .miles{
        height: 100%;
        background-color: var(--secondary-color);
        color: var(--secondary-color);
    }
    .buy-miles{
        height: 100%;
        background-color: #3781E6;
        color: #3781E6;
    }
    .goal{
        position: absolute;
        left: 70%;
        z-index: -1;
        font-size: 2rem;
        transform: translateY(-25%);
        color: #C4C4C4;
    }
</style>