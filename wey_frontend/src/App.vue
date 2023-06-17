<template>
    <NavBar />
    
    <main class="px-8 py-6 bg-gray-100">
        <RouterView />
    </main>
        
    <Footer />

    <Toast />
</template>

<script>
import Toast from '@/components/Toast.vue'
import Footer from '@/components/Footer.vue'
import NavBar from '@/components/NavBar.vue'

export default {
             
        components: {
            Toast,
            NavBar,
            Footer,
        },

        
    }
</script>

<style lang="scss">

main{
    background: rgb(50, 255, 19);
    background: linear-gradient(90deg, rgb(179, 241, 113) 0%, rgba(154, 232, 18, 0.234) 14%, rgb(186, 246, 171) 100%); 
}   

</style>