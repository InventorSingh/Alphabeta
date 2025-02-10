package bootiful.authorizationserver;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@Configuration
class UserDetailsConfiguration {

    @Bean
    UserDetailsService inMemoryUserDetailsManager() {
        var userBuilder = User.withDefaultPasswordEncoder();
        return new InMemoryUserDetailsManager(
                userBuilder.roles("USER").username("preet").password("password").build(),
                userBuilder.roles("USER", "ADMIN").username("ovais").password("p@ssw0rd").build()
        );
    }

}
