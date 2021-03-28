<script>
    export let user;
</script>

<div class="user-tile">
    <div class="user-icon">
        <!-- {user.pic} -->
    </div>
    <div class="user-name">
        {user.name}
    </div>
    <div class="percentage-paid">
        {user.percentageCompleted}%
    </div>
</div>

<style>
    .user-tile{
        background-color: var(--white);
        margin-bottom: 1rem;
        height: 3rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 2rem;
    }
    .user-icon{
        height: 2rem;
        width: 2rem;
        background-color: var(--main-color);
        border-radius: 50%;
    }
    .user-name{
        text-transform: capitalize;
        font-size: 1.2rem;
    }
</style>